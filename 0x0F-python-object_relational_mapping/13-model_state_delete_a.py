#!/usr/bin/python3
'''
script that deletes all State objects with a name containing the letter a
'''
from sqlalchemy import Column, Integer, String, create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states.all():
        session.delete(state)
    session.commit()
