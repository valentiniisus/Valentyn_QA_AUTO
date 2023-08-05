from modules.ui.page_objects.sign_in_page_ import Sign_In
import pytest


@pytest.mark.ui
def test_page_object():
    sign_in = Sign_In()

    sign_in.go_to()

    sign_in.try_login('valentiniisus', 'wrong password')

    assert sign_in.check_title('Sign in to GitHub · GitHub')

    sign_in.close()