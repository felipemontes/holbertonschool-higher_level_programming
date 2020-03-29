#!/usr/bin/python3
'''
script that adds the State object “Louisiana”
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

    newState = State(name='Louisiana')

    session.add(newState)
    session.commit()

    print(newState.id)
