from appium.webdriver.common.appiumby import AppiumBy

from locators.queries import button, secure_field, text_field


class LoginLocators:
    """Login screen. Fields have no accessibility identifier in Authentication.storyboard."""

    USERNAME = text_field()
    PASSWORD = secure_field()
    # Two Login buttons exist in the storyboard. The Face ID row is hidden
    # unless biometrics are enabled, so the visible one is the footer button.
    LOGIN_BUTTON = button("Login")
    # Container marked isElement on the More menu row.
    MENU_LOGIN = (AppiumBy.ACCESSIBILITY_ID, "Login Button")
