#!/usr/bin/python3
"""Module: 12-model_state_update_id
Links class to table in database, then updates query results
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, select)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    connection = engine.connect()
    Session = sessionmaker(bind=engine)

    session = Session()

    # query= session.query(Object).filter(Object.column.op('regexp')(REGEX))
    # query = session.query(State).filter(State.name.op('regexp')('a'))

    for record in session.query(State).all():
        if 'a' in record.name:
            session.delete(record)

    # commit deletions to the database
    session.commit()
