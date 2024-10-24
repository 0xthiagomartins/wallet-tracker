from sqlmodel_controller import BaseID
from sqlmodel import Field, Relationship
from pydantic import EmailStr


class User(BaseID, table=True):
    __tablename__ = "users"

    email: EmailStr = Field(
        nullable=False,
        unique=True,
        index=True,
        description="The user's unique email address.",
    )
    hashed_password: str = Field(
        nullable=False, description="The user's hashed password."
    )
