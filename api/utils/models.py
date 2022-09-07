from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from .constants import DEFAULT_TABLE

Base = declarative_base()

class Log(Base):
    """

    Description of logs table

    id : int
    time : year/day/hour/minute/second
    level : ERROR | WARNING | INFO | DEBUG
    text : str
    seconds : int

    """

    __tablename__ = DEFAULT_TABLE

    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    seconds = Column(Integer, nullable=False)
    level = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} (id={0.id!r}, time={0.time!r}, level={0.level!r}, text={0.text!r}, seconds={0.seconds!r})>".format(self)
