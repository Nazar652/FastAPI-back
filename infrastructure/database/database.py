from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
