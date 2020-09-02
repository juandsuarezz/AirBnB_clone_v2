#!/usr/bin/python3
"""City Module for HBNB project"""
import sqlalchemy
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            "Place", cascade='all, delete, delete-orphan', backref="cities")
    else:
        name = ''
        state_id = ''