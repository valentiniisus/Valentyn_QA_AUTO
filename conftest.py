import pytest
from modules.api.clients.github import GitHub


class User():

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Valentyn'
        self.second_name = 'Yushchyshyn'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user #Все що виконується до yield виконується до тесту, а все що після виконується після тесту

    user.remove()




    
@pytest.fixture
def github_api():
    api = GitHub()
    yield api





    
