#!/usr/bin/python3
'''
    Define the class City.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import State, Base


class City(Base):
    '''
        Define class City that imports from Base.
    '''
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
