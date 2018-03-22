#!/usr/bin/python3
'''
    script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City, Base
from relationship_state import State
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    # Create engine that opens connection between the class state and
    # the database with the data
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (uname, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new state and city with relationship
    new_state = State(name="California")
    new_state.cities = [City(name="San Francico")]
    session.add(new_state)
    session.commit()
