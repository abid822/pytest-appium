import pytest

from config.settings import settings
from data.catalog import USERNAME_REQUIRED, VALIDATION_TITLE


@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(catalog, login):
    # Step 1: Open Login from the More tab.
    catalog.wait_until_loaded()
    catalog.open_more()
    login.open_from_menu()
    # Step 2: Sign in with the demo account. A non-empty pair returns to the catalog.
    login.sign_in(settings.demo_username, settings.demo_password)
    catalog.wait_until_loaded()


@pytest.mark.login
@pytest.mark.regression
def test_invalid_login_shows_error(catalog, login):
    # Step 1: Open Login and submit the form with both fields empty.
    catalog.wait_until_loaded()
    catalog.open_more()
    login.open_from_menu()
    login.submit_empty()
    # Step 2: The app shows a validation alert. Empty username is checked first.
    message = login.error_message()
    assert VALIDATION_TITLE in message
    assert USERNAME_REQUIRED in message
