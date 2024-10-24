import os
from sqlmodel import SQLModel
from . import models, controllers, engine
from server import settings

# Conditionally create tables based on the environment
if settings.ENVIRONMENT in {"production", "development", "stage"}:
    SQLModel.metadata.create_all(engine.get_engine())
elif settings.ENVIRONMENT == "test":
    # Do not create tables automatically in test environment
    pass
else:
    raise ValueError(f"Unsupported environment: {settings.ENVIRONMENT}")
