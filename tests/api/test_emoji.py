import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_emoji_get1(github_api):
    user = github_api.search_emoji()
    assert user['+1'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8'

@pytest.mark.api
def test_emoji_get2(github_api):
    user = github_api.search_emoji()
    assert user['-1'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f44e.png?v8'

@pytest.mark.api
def test_emoji_get3(github_api):
    user = github_api.search_emoji()
    assert user['100'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8'


