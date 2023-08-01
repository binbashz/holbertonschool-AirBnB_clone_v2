#!/usr/bin/python3
"""DBStorage Module for HBNB project"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel

class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects in the current database session"""
        from models import storage
        obj_dict = {}
        if cls:
            for obj in self.__session.query(cls):
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            for cls in storage.classes:
                if issubclass(storage.classes[cls], BaseModel):
                    for obj in self.__session.query(storage.classes[cls]):
                        key = f"{obj.__class__.__name__}.{obj.id}"
                        obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
