
import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movies_dao_fixture():
    movies_dao = MovieDAO(None)

    # m1 = Movie(id=1, title="Movie1", description="Description1", trailer=111)
    # m2 = Movie(id=2, title='Movie2', description='Description2', trailer=222)

    m1 = Movie(id=1, title='Movie1', description='Joan', trailer=111, year=1990, rating=400, genre_id=1, director_id=1)
    m2 = Movie(id=2, title='Movie2', description='Dyuma', trailer=123, year=1510, rating=1344, genre_id=2, director_id=1)


    movies_dao.get_one = MagicMock(return_value=m1)
    movies_dao.get_all = MagicMock(return_value=[m1, m2])

    return movies_dao


class TestMoviesServices:
    @pytest.fixture(autouse=True)
    def movies_service(self, movies_dao_fixture):
        self.movies_service = MovieService(dao=movies_dao_fixture)

    def test_get_one(self):
        movie = self.movies_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movies_service.get_all()
        assert len(movies) > 0

