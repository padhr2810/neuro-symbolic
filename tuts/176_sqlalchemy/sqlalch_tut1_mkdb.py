
"""
https://www.youtube.com/watch?v=Z2zD3EdjpNo&list=PLKm_OLZcymWhtiM-0oQE2ABrrbgsndsn0&index=1
Zeq Tech
 Python SQLAlchemy ORM - The BEST Introduction
"""

from sqlalchemy import URL, create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

url_object = URL.create(
    "sqlite",
    database="ep_01_database.db",
)

# Create an engine for a SQLite database
engine = create_engine(url_object)
# or
# engine = create_engine("sqlite:///ep_01_database.db.db")

# Create a base class for our models
Base = declarative_base()

# Define a model for the "users" table
class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    patient_age = Column(Integer)

# Create the database tables
Base.metadata.create_all(engine)

