import model
import csv
from datetime import datetime

def load_users(session):
    # use u.user
    with open('seed_data/u.user') as csvfile:
        user_reader = csv.reader(csvfile, delimiter='|')
        for row in user_reader:
            # print ', '.join(row)
            id = row[0]
            age = row[1]
            gender = row[2]
            position = row[3]
            zipcode = row[4]
            new_object = model.User(age=age, email='null', password='null', zipcode=zipcode)
            session.add(new_object)           
        session.commit()

    # id = Column(Integer, primary_key = True) # this defines id as primary key
    # email = Column(String(64), nullable = True) # this defines optional string
    # password = Column(String(64), nullable = True) # this defines optional string
    # age = Column(Integer, nullable = True) # this defines integer for age
    # zipcode = Column(String(15), nullable = True) # this defines string for zipcode
    # # This creates a relationship to Rating
    # ratings = relationship("Rating")


def load_movies(session):
    # use u.item
    with open('seed_data/u.item') as csvfile:
        user_reader = csv.reader(csvfile, delimiter='|')
        for row in user_reader:
            print ', '.join(row)
            id = row[0]
            titledate = row[1].split(' (')
            title = titledate[0].decode("latin-1")
            releasetime = row[2]
            if releasetime == '':
                continue
            release_date = datetime.strptime(releasetime, "%d-%b-%Y")
            link = row[4]
            movie = model.Movie(name=title, released_at=release_date, imdb_url=link)
            session.add(movie)
        session.commit()

    # id = Column(Integer, primary_key = True)
    # name = Column(String(64), nullable = True)
    # released_at = Column(DATETIME)
    # imdb_url = Column(String(64), nullable = True)
    # # this creates a relationship to Rating
    # ratings = relationship("Rating")

def load_ratings(session):
    # use u.data
    with open('seed_data/u.data') as csvfile:
        user_reader = csv.reader(csvfile, delimiter='\t')
        for row in user_reader:
            print ', '.join(row)
            user_id = row[0]
            movie_id = row[1]
            rating = row[2]
            rating_object = model.Rating(user_id=user_id, movie_id=movie_id, rating=rating)
            session.add(rating_object)
        session.commit()

    # id = Column(Integer, primary_key = True)
    # movie_id = Column(Integer, ForeignKey('movies.id'))
    # user_id = Column(Integer, ForeignKey('users.id'))
    # rating = Column(Integer, nullable = True)


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s = model.connect()
    main(s)
