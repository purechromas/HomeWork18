from dao.models.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Director).get(gid)

    def get_all(self):
        return self.session.query(Director).all()
