from .models import User
from sqlmodel_controller import Controller
from . import engine


user = Controller[User](engine=engine.get())
