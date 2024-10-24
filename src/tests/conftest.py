import sys, os
from pathlib import Path


# Add the parent directory to sys.path to configure imports from one folder above
sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ["ENVIRONMENT"] = "test"

import pytest
from sqlmodel import SQLModel
from server import db


@pytest.fixture(scope="session")
def test_engine():
    engine = db.engine.get()
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()
    SQLModel.metadata.drop_all(engine)
