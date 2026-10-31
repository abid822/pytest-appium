from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException

from locators.login_locators import LoginLocators
from locators.menu_locators import MenuLocators
from locators.queries import Locator
from screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    """More menu login row, then the username and password form."""

    def open_from_menu(self) -> None:
        # The row button is LogOut-menu-item. The container is "Login Button".
        self._bring_into_view(MenuLocators.LOGOUT_ROW)
        self.tap(MenuLocators.LOGOUT_ROW)
        self.find_visible(LoginLocators.USERNAME)

    def _bring_into_view(self, locator: Locator) -> None:
        shown = [item for item in self.driver.find_elements(*locator) if item.is_displayed()]
        if shown or locator[0] != AppiumBy.ACCESSIBILITY_ID:
            return
        try:
            self.driver.execute_script(
                "mobile: scroll",
                {"direction": "down", "predicateString": f'name == "{locator[1]}"'},
            )
        except WebDriverException:
            return

    def sign_in(self, username: str, password: str) -> None:
        # Step 1: Fill both fields. The screen accepts any non-empty pair.
        self.type_text(LoginLocators.USERNAME, username)
        self.type_text(LoginLocators.PASSWORD, password)
        # Step 2: Dismiss the keyboard so the footer Login button can be tapped.
        self.hide_keyboard()
        self.tap(LoginLocators.LOGIN_BUTTON)

    def submit_empty(self) -> None:
        # Leave both fields blank and tap Login.
        self.hide_keyboard()
        self.tap(LoginLocators.LOGIN_BUTTON)

    def error_message(self) -> str:
        return self.accept_alert()
