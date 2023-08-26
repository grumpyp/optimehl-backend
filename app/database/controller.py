import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///app/database/optimehl.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

TASKS = {
    ('Paper_1','Blue')   : {'dur': 45},
    ('Paper_1','Yellow') : {'dur': 10},
    ('Paper_2','Blue')   : {'dur': 20},
    ('Paper_2','Green')  : {'dur': 10},
    ('Paper_2','Yellow') : {'dur': 34},
    ('Paper_3','Blue')   : {'dur': 12},
    ('Paper_3','Green')  : {'dur': 17},
    ('Paper_3','Yellow') : {'dur': 28},
}