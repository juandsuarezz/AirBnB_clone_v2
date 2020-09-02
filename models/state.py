#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")

    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id
            equals to the current State.id"""
            instance_list = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == 'City':
                    if obj.state_id == self.id:
                        instance_list.append(obj)
            return instance_list
