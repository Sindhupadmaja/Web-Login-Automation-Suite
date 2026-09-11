import pytest
from utils.test_data import *

@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.is_logged_in()

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("username", INVALID_USERNAMES)
def test_invalid_username(login_page, username):
    login_page.login(username, VALID_PASSWORD)
    assert login_page.error_message()

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("password", INVALID_PASSWORDS)
def test_invalid_password(login_page, password):
    login_page.login(VALID_USERNAME, password)
    assert login_page.error_message()

@pytest.mark.regression
@pytest.mark.validation
@pytest.mark.parametrize(("username", "password"), [
    ("", VALID_PASSWORD), (VALID_USERNAME, ""), ("", "")
])
def test_required_fields(login_page, username, password):
    login_page.login(username, password)
    assert login_page.error_message()

@pytest.mark.regression
def test_locked_out_user(login_page):
    login_page.login(LOCKED_USERNAME, VALID_PASSWORD)
    assert "locked" in login_page.error_message().lower()

@pytest.mark.regression
@pytest.mark.boundary
@pytest.mark.parametrize(("username", "password"), [
    (LONG_USERNAME, VALID_PASSWORD), (VALID_USERNAME, LONG_PASSWORD)
])
def test_long_input_is_handled(login_page, username, password):
    login_page.login(username, password)
    assert login_page.error_message()
