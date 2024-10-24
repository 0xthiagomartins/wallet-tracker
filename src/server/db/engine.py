from sqlmodel import create_engine
from sqlmodel.pool import StaticPool
import os

production = create_engine("sqlite:///wallet_tracker.db")
test = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
development = create_engine("sqlite:///wallet_tracker.db", echo=True)


def get():
    ENVIRONMENT = os.getenv("ENVIRONMENT", "test")
    match ENVIRONMENT:
        case "production":
            return production
        case "development":
            return development
        case "test":
            return test
        case "stage":
            pass
