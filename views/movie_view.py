from flask_restx import Resource, Namespace
from flask import request

from service_container import movie_service
from dao.models.movie_model import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data_director_id = request.args.get('director_id')
        data_genre_id = request.args.get('genre_id')
        data_year = request.args.get('year')
        if data_director_id:
            movie = movie_service.get_movie_by_director(data_director_id)
            return movies_schema.dump(movie), 200
        elif data_genre_id:
            movie = movie_service.get_movie_by_genre(data_genre_id)
            return movies_schema.dump(movie), 200
        elif data_year:
            movie = movie_service.get_movie_by_year(data_year)
            return movies_schema.dump(movie), 200
        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        movie_service.create(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        movie_service.update(data, mid)
        return '', 204

    def patch(self, mid):
        data = request.json
        movie_service.update(data, mid)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
