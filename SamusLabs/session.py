from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import pymysql

Base = declarative_base()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='samusdb',
    charset='utf8mb4',
)

engine = create_engine(
    f"mysql+pymysql://{connection.user}:{connection.password}"
    f"@{connection.host}:{connection.port}/samusdb"
)

sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


class Base(DeclarativeBase):
    pass


# @contextmanager
def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()