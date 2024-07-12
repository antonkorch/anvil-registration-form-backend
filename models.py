# Description: This file contains the model classes for the database.
from sqlalchemy.orm import DeclarativeBase, mapped_column, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = 'clients'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    company = mapped_column(String)
    city = mapped_column(String)
    phone = mapped_column(String)
    email = mapped_column(String)
