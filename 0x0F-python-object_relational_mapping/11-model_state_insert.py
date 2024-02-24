#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State
from relationship_city import Base, City


def insert_state(username, password, database_name):
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
