from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import time

from faker import Faker

from .models import Log
from .constants import DEFAULT_TABLE

LEVELS = ['ERROR', 'WARNING', 'INFO', 'DEBUG']

fake = Faker()
Base = declarative_base()

TABLES = {
    DEFAULT_TABLE: Log
}


def create_session(link: str) -> "Session":
    """
    Create session to provide interaction with database
    """
    _session_factory = sessionmaker(create_engine(link))

    return scoped_session(_session_factory)


def get_table(tablename: str):
    if tablename in TABLES:
        return TABLES[tablename]

    class SelectedTable(Base):
        __tablename__ = tablename
        __table_args__ = {'extend_existing': True}

        id = Column(Integer, nullable=False, unique=True,
                    primary_key=True, autoincrement=True)
        time = Column(String, nullable=False)
        seconds = Column(Integer, nullable=False)
        level = Column(String, nullable=False)
        text = Column(String, nullable=False)

    Base.metadata.create_all(engine)
    TABLES[tablename] = SelectedTable

    return SelectedTable


def get_tables() -> list:
    inspector = inspect(engine)
    return inspector.get_table_names()


def get_last_id(_session: "Session", tablename: str) -> int:
    _table = get_table(tablename)
    count_query = select([func.count()]).select_from(_table)
    count = _session.execute(count_query).scalar()

    return count


def _get_logs(
        _session: "Session",
        levels: str,
        text: str,
        seconds: list,
        table_name: str,
        offset: int,
        limit: int,
        from_id: int) -> list:
    """
    Get logs from database

    :return:

    ScalarResult <---> list of Log objects

    """

    if table_name not in engine.table_names():
        raise Exception(f'Undefined table name : {table_name}')

    _table = get_table(table_name)
    logs = select(_table)

    if not limit:
        limit = 10

    if offset is None:
        offset = 0

    if from_id is None:
        from_id = limit

    if levels:
        logs = logs.where(_table.level.in_(levels))

    if text:
        logs = logs.where(_table.text.contains(text))

    if seconds:
        logs = logs.where(_table.seconds >= seconds[0]).where(
            _table.seconds <= seconds[1])

    logs = logs.where(_table.id <= (from_id - offset)
                        ).where(_table.id > (from_id - offset - limit))

    print(from_id)

    return _session.scalars(logs)


def get_logs(
        _session: "Session",
        levels: str,
        limit: int,
        text: str,
        seconds: list,
        table_name: str,
        offset: int,
        from_id: int) -> list[dict]:
    """
    Convert list of log objects to list of dictionaries
    """

    if not levels:
        levels = LEVELS

    if not table_name:
        table_name = DEFAULT_TABLE

    logs = _get_logs(_session, levels, text, seconds,
                     table_name, offset, limit, from_id)
    converted_logs: list[dict] = list()

    if not limit:
        limit = 10 ** 4

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


def generate_log(_session: "Session", table_name: str, level: str, content: str) -> Log:
    """ Generate one log and add to the database """
    y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime()

    if table_name not in engine.table_names():
        raise Exception(f'Undefined table name : {table_name}')

    CurrentTable = get_table(table_name)

    current_time = f"{y}/{m}/{d}/{hh}/{mm}/{ss}"
    seconds_time = int(time.time())

    log = CurrentTable(time=current_time, level=level,
                       text=content, seconds=seconds_time)

    _session.add(log)
    _session.commit()

    return log
