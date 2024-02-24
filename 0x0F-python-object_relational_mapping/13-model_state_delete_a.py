#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qu = session.query(State)
    states_to_delete = qu.filter(State.name.like("%a%")).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
