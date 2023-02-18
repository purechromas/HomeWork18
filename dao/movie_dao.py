from dao.models.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movie_by_director(self, data):
        return self.session.query(Movie).filter_by(director_id=data)

    def get_movie_by_genre(self, data):
        return self.session.query(Movie).filter_by(genre_id=data)

    def get_movie_by_year(self, data):
        return self.session.query(Movie).filter_by(year=data)

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
