from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URL = config["DB"]
ALGORITHM = "HS256"
SECRET_KEY = config["SECRET_KEY"]
ACCESS_TOKEN_EXPIRE_MINUTES = 30
