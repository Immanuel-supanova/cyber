from pydantic import BaseModel

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str

class UserAuthenticate(UserCreate):
    pass

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    is_staff: bool

    class Config:
        orm_mode = True

class UserEmailChange(BaseModel):
    old_email: str 
    new_email: str

class UserPasswordChange(UserBase):
    old_password: str
    new_password: str
    confirm_password: str

class UserIsActiveChange(UserBase):
    is_active: bool

class UserIsStaffChange(UserBase):
    is_staff: bool