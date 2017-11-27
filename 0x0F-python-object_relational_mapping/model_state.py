#!/usr/bin/python3

''' module: model_state
includes object models of tables in a MySQL database
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''A class that inherits from declarative_base in the land of SQLAlchemy
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
