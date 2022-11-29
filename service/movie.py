from flask import request

from constants import PWD_LIMIT
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, status, page):
        movies = self.dao.get_movie()

        if status and status == "new":
            movies = self.dao.get_new(movies)

        if page:
            limit = PWD_LIMIT
            offset = (int(page)-1)*limit
            movies = self.dao.get_page(movies, limit, offset)

        movies = self.dao.get_all(movies)

        return movies

