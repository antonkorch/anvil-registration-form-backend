# Description: This file contains the functions that interact with the database.
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models import Client

def create_db (engine):
    Client.metadata.create_all(engine)

def drop_db (engine):
    Client.metadata.drop_all(engine)

def add_client (engine, name, company, city, phone, email):
    Session = sessionmaker(bind=engine)
    session = Session()
    client = Client(name=name, email=email, phone=phone, city=city, company=company)
    session.add(client)
    session.commit()
    session.close()