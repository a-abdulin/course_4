from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movie(self):
        return self.session.query(Movie)

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, query):
        return query.all()

    def get_new(self, query):
        movies = query.order_by(desc(Movie.year))
        return movies

    def get_page(self, query, limit, offset):
        movies = query.limit(limit).offset(offset)
        return movies

