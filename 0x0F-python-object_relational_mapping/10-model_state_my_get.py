#!/usr/bin/python3
'''
    script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State, Base
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]
    # Create engine that opens connection between the class state and
    # the database with the data
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (uname, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    query = session.query(State).filter(State.name == search_name)
    if query.count() == 0:
        print("Not found")
    for instance in query:
        print(instance.id)
