#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qu = session.query(City, State)
    filte_ = qu.filter(City.state_id == State.id).order_by(City.id)

    for city, state in filte:
        print("{state.name}: ({city.id}) {city.name}")
