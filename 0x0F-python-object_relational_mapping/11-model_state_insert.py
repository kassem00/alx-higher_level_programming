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

def create_state_city(username, password, database_name):
    # Create engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}", pool_pre_ping=True)
    
    # Create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add State and City to the session
    session.add(City(name="San Francisco", state=State(name="California")))

    # Commit changes
    session.commit()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    create_state_city(sys.argv[1], sys.argv[2], sys.argv[3])
