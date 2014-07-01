from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.sqlite import DATETIME
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

### Class declarations go here
class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True) # this defines id as primary key
	email = Column(String(64), nullable = True) # this defines optional string
	password = Column(String(64), nullable = True) # this defines optional string
	age = Column(Integer, nullable = True) # this defines integer for age
	zipcode = Column(String(15), nullable = True) # this defines string for zipcode
	# This creates a relationship to Rating
	ratings = relationship("Rating")

class Movie(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = True)
	released_at = Column(DATETIME)
	imdb_url = Column(String(64), nullable = True)
	# this creates a relationship to Rating
	ratings = relationship("Rating")

class Rating(Base):
	__tablename__ = "ratings"

	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer, ForeignKey('movies.id'))
	user_id = Column(Integer, ForeignKey('users.id'))
	rating = Column(Integer, nullable = True)

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
