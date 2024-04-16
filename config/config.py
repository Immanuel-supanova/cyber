import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

DATABASE_URL = os.getenv("DB")
ALGORITHM = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
