from sqlmodel import SQLModel, create_engine
from . import models, controllers, engine


SQLModel.metadata.create_all(engine.get())
