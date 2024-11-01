
from sqlalchemy import (URL, Column, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.orm import declarative_base

url_object = URL.create(
    "sqlite",
    database="ep_04_database.db",
)
# or
# engine = create_engine("sqlite:///ep_04_database.db.db")

# Create an engine for a SQLite database
engine = create_engine(url_object)

# Create a base class for our models
Base = declarative_base()

# Define a model for the "users" table
class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    patient_age = Column(Integer)

    def __repr__(self) -> str:
        return f"<Patient id: {self.patient_id:>3}: name: {self.patient_name:<13}, age: {self.patient_age:>3}>"

# create the database tables
Base.metadata.create_all(engine)

