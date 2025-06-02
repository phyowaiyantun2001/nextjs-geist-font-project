import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from a .env file if available

MYSQL_USER = os.getenv("MYSQL_USER", "lms_user")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "lms_pass")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB", "lms_db")
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "YOUR_SECRET_KEY")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
