from datetime import datetime, timedelta, timezone
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Session
from config.config import SECRET_KEY, ALGORITHM
from database.database import Base, SessionLocal
from passlib.context import CryptContext
from schema.users import UserAuthenticate, UserCreate, UserEmailChange, UserIsActiveChange, UserIsStaffChange, UserPasswordChange, User as UserMain
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Annotated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)


class UserQuery(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, password=hashed_password)
        self.db.add(db_user)
        self.db.commit()

    def create_staff(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, password=hashed_password, is_staff=True)
        self.db.add(db_user)
        self.db.commit()
    
    def create_admin(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email=user.email, password=hashed_password, is_admin=True)
        self.db.add(db_user)
        self.db.commit()
    
    def email_change(self, user: UserEmailChange):
        user = self.get_user_by_email(user.old_email)
        self.db.query(user).update({"email": user.new_email})
        self.db.commit()
    
    def password_change(self, user: UserPasswordChange):  
        user2 = self.get_user_by_email(user.email)
        
        if verify_password(user.old_password, user2.password) == False:
            return None
        
        if user.new_password != user.confirm_password:
            return None

        hashed_new_password = get_password_hash(user.new_password)

        self.db.query(user2).update({"password": hashed_new_password})
        self.db.commit()
    
    def is_active_change(self, user: UserIsActiveChange):
        user2 = self.get_user_by_email(user.email)
        self.db.query(user2).update({"is_active": user.is_active})
        self.db.commit()
    
    def is_staff_change(self, user: UserIsStaffChange):
        user2 = self.get_user_by_email(user.email)
        self.db.query(user2).update({"is_staff": user.is_staff})
        self.db.commit()
    
    def get_users(self):
        return self.db.query(User)
    
    def get_user(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def authenticate_user(self, user: UserAuthenticate):
        user2 = self.get_user_by_email(user.email)
        if not user:
            return False
        if not verify_password(user.password, user2.hashed_password):
            return False
        return user

query = UserQuery(db=SessionLocal)
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("id")
        if id is None:
            raise credentials_exception
        token_data = UserMain(id=id)
    except JWTError:
        raise credentials_exception
    user = query.get_user(id=token_data.id)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user