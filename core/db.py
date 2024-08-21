import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine(
            'mysql+pymysql://{}:{}@{}/{}'
            .format('url_dev', 'url_dev_pwd', 'localhost', 'url_dev_db')
        )
        self.reload()  # Initialize the session here
    
    def new(self, obj):
        """Add the object to the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized.")
        print(obj)
        self.__session.add(obj)
        
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, short_code):
        """Get the instance of link"""
        instance = self.__session.query(cls).filter_by(short_code=short_code).first()
        return instance
        
    def count(self, cls):
        """Return the count of saved links"""
        instances = self.__session.query(cls).all()
        return len(instances)
