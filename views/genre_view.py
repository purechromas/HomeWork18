from flask_restx import Resource, Namespace

from service_container import genre_service
from dao.models.genre_model import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        one_genre = genre_service.get_one(gid)
        print(one_genre)
        return genre_schema.dump(one_genre), 200
