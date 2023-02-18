from flask import Flask
from flask_restx import Api

from configuration import Config
from database import db
from views.director_view import director_ns
from views.genre_view import genre_ns
from views.movie_view import movie_ns
from dao.models.movie_model import Movie
from dao.models.genre_model import Genre
from dao.models.director_model import Director

app = Flask(__name__)


def flask_configuration(application: Flask):
    application.config.from_object(Config)
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    print("Configuration was successful")


def load_data():
    m1 = Movie(title='The Shawshank Redemption',
               description='description',
               trailer='www.trailer.com',
               year=1994,
               rating=9.4,
               genre_id=1,
               director_id=1)
    m2 = Movie(title='The Godfather',
               description='description',
               trailer='www.trailer.com',
               year=1972,
               rating=9.2,
               genre_id=2,
               director_id=2)
    g1 = Genre(name='Drama')
    g2 = Genre(name='Crime')
    d1 = Director(name='Frank Darabont')
    d2 = Director(name='Francis Ford Coppola')

    with app.app_context():
        db.create_all()
        db.session.add_all([m1, m2, g1, g2, d1, d2])
        db.session.commit()
    print("Loading data was successful")


if __name__ == '__main__':
    flask_configuration(app)
    load_data()
    app.run()
