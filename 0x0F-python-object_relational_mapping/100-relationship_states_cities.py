#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
Usage: ./100-relationship_states_cities.py <mysql username> /
                                           <mysql password> /
                                           <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)

    session.commit()
    session.close()

if __name__ == "__main__":
    main()
