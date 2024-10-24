import pytest
from server.auth import Auth, AuthenticationError, AuthorizationError
from server.config import SECRET_KEY


def test_register_user():
    auth = Auth(secret_key=SECRET_KEY)
    user = auth.register_user("test@example.com", "password123")
    assert user.get("email") == "test@example.com"
    assert user.get("hashed_password") != "password123"


def test_login_user():
    auth = Auth(secret_key=SECRET_KEY)
    token = auth.login_user("test@example.com", "password123")
    assert isinstance(token, str)


def test_register_existing_user():
    auth = Auth(secret_key=SECRET_KEY)
    with pytest.raises(AuthenticationError):
        auth.register_user("test@example.com", "newpassword")


def test_login_invalid_credentials():
    auth = Auth(secret_key=SECRET_KEY)
    with pytest.raises(AuthorizationError):
        auth.login_user("test@example.com", "wrongpassword")
