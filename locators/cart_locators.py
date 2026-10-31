from appium.webdriver.common.appiumby import AppiumBy

from locators.queries import Locator, static_text


class CartLocators:
    """Cart tab and cart screen."""

    SCREEN = (AppiumBy.ACCESSIBILITY_ID, "Cart-screen")
    TAB = (AppiumBy.ACCESSIBILITY_ID, "Cart-tab-item")
    # cartCountLbl has no accessibility identifier. Its name is the count, it
    # sits on the cart tab, and XCUITest reports it as not visible.

    @staticmethod
    def items_count(count: int) -> Locator:
        # MyCartViewController sets totalItemLbl to "{count} Items".
        return static_text(f"{count} Items")
