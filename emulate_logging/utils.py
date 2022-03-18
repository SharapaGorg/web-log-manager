from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import time
import random

from faker import Faker

from config import LINK

levels_ = ['ERROR', 'WARNING', 'INFO', 'DEBUG']

engine = create_engine(LINK)
Session = sessionmaker(engine)
Base = declarative_base()

fake = Faker()

class Log(Base):
    """

    Description of logs table

    id : int
    time : year/day/hour/minute/second
    level : ERROR | WARNING | INFO | DEBUG
    text : str
    seconds : int

    """

    __tablename__ = "logs"

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    seconds = Column(Integer, nullable=False)
    level = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} (id={0.id!r}, time={0.time!r}, level={0.level!r}, text={0.text!r}, seconds={0.seconds!r})>".format(self)

def create_session(link : str) -> Session:
    """
    Create session to provide interaction with database
    """
    _session_ = sessionmaker(create_engine(link))

    return _session_()

def _get_logs(_session : Session, levels : str) -> list:
    """
    Get logs from database

    :return:

    ScalarResult <---> list of Log objects

    """

    if levels:
        logs = select(Log).where(Log.level.in_(levels))
    else:
        logs = select(Log)

    return _session.scalars(logs)

def get_logs(_session : Session, levels : str, limit : int) -> list[dict]:
    """
    Convert list of log objects to list of dictionaries
    """

    if not levels:
        levels = levels

    logs = _get_logs(_session, levels)
    converted_logs : list[dict] = list()

    ignore_vars = ['_sa_instance_state']
    counter = int()

    for log in logs:
        if counter == limit:
            break

        converted_log = dict()

        for var in vars(log):
            if var not in ignore_vars:
                converted_log[var] = getattr(log, var)

        counter += 1
        converted_logs.append(converted_log)

    return converted_logs

def generate_logs(_session : Session, count : int):
    """
    Generate logs and add them to database
    """

    for i in range(count):
        y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime()

        current_time = f"{y}/{m}/{d}/{hh}/{mm}/{ss}"
        seconds_time = int(time.time())

        log = Log(time=current_time, level=random.choice(levels), text=fake.sentence(10), seconds=seconds_time)

        _session.add(log)

    _session.commit()

Base.metadata.create_all(engine)