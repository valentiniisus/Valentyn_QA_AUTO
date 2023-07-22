import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_my_repo(github_api):
    user = github_api.github_comits_request()
    assert user[0]['commit']['author']['name'] == 'valentiniisus' #так як воно при респонсі повертає список то звертаємось до першого елемента списку
