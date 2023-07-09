import pytest

@pytest.mark.check #останнє це імя групи
def test_check_name(user):
    assert user.name == 'Valentyn'

@pytest.mark.check
def test_check_second_name(user):
    assert user.second_name == 'Yushchyshyn'
