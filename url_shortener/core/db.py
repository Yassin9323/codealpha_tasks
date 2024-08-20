#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None
    
    def __init__(self):
        
         self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format('url_dev',
                                            'url_dev_pwd',
                                            'localhost',
                                            'url_dev_db'))
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, short_code):
        """ get the instance of link """
        instance = self.__session.query(cls).filter_by(short_code=short_code).first()
        print(instance.__dict__)
        return instance
        
    def count(self, cls):
        """ return the count of saved links """
        instances = self.__session.query(cls).all()
        return len(instances)
