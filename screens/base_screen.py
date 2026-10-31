from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import settings
from locators.queries import Locator


class BaseScreen:
    """Shared driver helpers. All screen objects inherit this."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.explicit_wait_seconds)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: Locator) -> WebElement:
        def _visible(driver: WebDriver) -> WebElement | bool:
            for element in driver.find_elements(*locator):
                if element.is_displayed():
                    return element
            return False

        return self.wait.until(_visible)

    def find_displayed(self, locator: Locator) -> list[WebElement]:
        def _shown(driver: WebDriver) -> list[WebElement] | bool:
            shown = [
                element for element in driver.find_elements(*locator) if element.is_displayed()
            ]
            return shown or False

        return self.wait.until(_shown)

    def tap(self, locator: Locator) -> None:
        displayed = self.find_displayed(locator)
        if not displayed:
            raise AssertionError(f"No visible element for {locator}")
        displayed[0].click()

    def type_text(self, locator: Locator, value: str) -> None:
        element = self.find_visible(locator)
        element.click()
        try:
            element.clear()
        except WebDriverException:
            pass
        element.send_keys(value)

    def text_of(self, element: WebElement) -> str:
        identifier = (element.get_attribute("name") or "").strip()
        candidates = [
            (element.get_attribute("value") or "").strip(),
            (element.get_attribute("label") or "").strip(),
            (element.text or "").strip(),
        ]
        for candidate in candidates:
            if candidate and candidate != identifier:
                return candidate
        return next((candidate for candidate in candidates if candidate), "")

    def visible_text(self, locator: Locator) -> str:
        return self.text_of(self.find_visible(locator))

    def visible_texts(self, locator: Locator) -> list[str]:
        texts: list[str] = []
        for element in self.find_displayed(locator):
            text = self.text_of(element)
            if text:
                texts.append(text)
        return texts

    def hide_keyboard(self) -> None:
        try:
            self.driver.hide_keyboard()
        except WebDriverException:
            return

    def accept_alert(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text or ""
        alert.accept()
        return text
