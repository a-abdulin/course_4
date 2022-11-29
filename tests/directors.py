
import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Semen Petrovich")
    d2 = Director(id=1, name="Pavel Ivanovich")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.name == "Semen Petrovich"

    def test_get_all(self):
        director = self.director_service.get_all()
        assert director != None
        assert director[-1].name == "Pavel Ivanovich"
        assert len(director) > 0
