import os
from dotenv import load_dotenv

load_dotenv()

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30