import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exist(github_api):
    api = GitHub()
    # user = api.get_user_defunkt()
    # user = api.get_user('defunkt')
    user = github_api.get_user('defunkt')


    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_get_user_nonexist(github_api):
    # user = api.get_user_nonexist()
    # user = api.get_user('valentyn_yushchyshyn')
    user = github_api.get_user('valentyn_yushchyshyn')


    # print(user) #-s пишемо в консолі, означає що в консолі виведеться умовно кажучи цей прінт. 
    #Після чого в вікні яке виводиться бачимо повідомлення :
    # {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/users/users#get-a-user'}
    #З нього беремо ключ і значення для асерту

    assert user['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('Valentyn_QA_AUTO')
    assert r['total_count'] == 1
    assert 'Valentyn_QA_AUTO' in r['items'][0]['name'] #в списку айтемс має бути назва репозиторію перша за ключем name


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('Valentyn_QA_AUTO_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('v')
    assert r['total_count'] != 0

   

