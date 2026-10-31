from appium.webdriver.common.appiumby import AppiumBy

from locators.queries import Locator, static_text


class CartLocators:
    """Cart tab and cart screen."""

    SCREEN = (AppiumBy.ACCESSIBILITY_ID, "Cart-screen")
    TAB = (AppiumBy.ACCESSIBILITY_ID, "Cart-tab-item")
    # The badge label has no accessibility identifier. It sits in the cart tab,
    # in the view just before the Cart-tab-item button. Hidden while the count is 0.
    BADGE = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Cart-tab-item"]'
        "/preceding-sibling::XCUIElementTypeOther[1]"
        "//XCUIElementTypeStaticText",
    )

    @staticmethod
    def items_count(count: int) -> Locator:
        # MyCartViewController sets totalItemLbl to "{count} Items".
        return static_text(f"{count} Items")
