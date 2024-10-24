from sqlmodel import create_engine
import os


production = create_engine("sqlite:///wallet_tracker.db")
development = create_engine("sqlite:///wallet_tracker.db", echo=True)


def get():
    is_production = os.getenv("PROD", False)
    engine = production if is_production else development
    return engine
