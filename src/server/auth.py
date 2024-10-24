from .db import models, controllers
import bcrypt, jwt
from datetime import datetime, timedelta, timezone
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


class AuthenticationError(Exception):
    """Exception raised for authentication failures."""

    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message)


class AuthorizationError(Exception):
    """Exception raised for authorization failures."""

    def __init__(self, message: str = "Authorization failed"):
        super().__init__(message)


class Auth:
    def __init__(self, secret_key: str = SECRET_KEY):
        self.secret_key = secret_key
        self.algorithm = ALGORITHM
        self.access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    def register_user(self, email: str, password: str) -> models.User:
        with controllers.user as c_user:
            user_id = c_user.get(by=["email", "archived"], value=[email, False])
            if user_id:
                raise AuthenticationError("User already exists")
            hashed_password = self.__hash_password(password)
            new_user = c_user.create(
                dict(email=email, hashed_password=hashed_password), returns_object=True
            )
        return new_user

    def login_user(self, email: str, password: str) -> str:
        user = controllers.user.get(by=["email", "archived"], value=[email, False])
        if not user or not self.__verify_password(
            password, user.get("hashed_password")
        ):
            raise AuthorizationError("Invalid credentials")
        token = self.__create_jwt_token(user)
        return token

    def __hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    def __verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    def __create_jwt_token(self, user: models.User) -> str:
        expire = datetime.now(timezone.utc) + self.access_token_expire
        to_encode = {"sub": user.get("email"), "exp": expire}
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
