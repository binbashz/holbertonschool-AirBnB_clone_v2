#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os

env = os.getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if env == 'db':
        city_id = Column(String(60), ForeignKey('cities.id') ,nullable=False)
        user_id = Column(String(60), ForeignKey('users.id') ,nullable=False)
        name = Column(String(128) ,nullable=False)
        description = Column(String(1024) ,nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)

        reviews = relationship('Review', cascade="all, delete, delete-orphan",
                               backref='place')

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
            from models.review import Review
            from models import storage

            results = []
            for element in storage.all(Review).values():
                if self.id == element.place_id:
                    results.append(storage.all(Review)[element])
            return results
