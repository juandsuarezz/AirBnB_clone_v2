#!/usr/bin/python3
""" Place Module for HBNB project """
import sqlalchemy
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table

place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship(
            "Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            ''' Relation with reviews '''
            instance_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    instance_list.append(review)
            return instance_list

        @property
        def amenities(self):
            ''' Relation with amenities '''
            instance_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    instance_list.append(review)
            return instance_list

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
            else:
                pass
