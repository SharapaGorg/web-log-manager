from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import LINK
from utils import Base
import os


# dev (local) mode
engine = create_engine(f"sqlite:///base")

# prod (remote) mode
# engine = create_engine(LINK)

Base.metadata.create_all(engine)

if not os.path.isfile('./base'):
    Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# ------ MODELS ------