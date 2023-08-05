#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

env = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if env == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        name = ""
        @property
        def cities(self):
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(storage.all(City)[city])
            return city_list
