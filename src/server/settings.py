import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ENVIRONMENT = os.getenv("ENVIRONMENT", "test")
