from appium.webdriver.common.appiumby import AppiumBy

from locators.queries import Locator, static_text


class ProductLocators:
    """Product detail. Ids are from TabBar.storyboard unless noted."""

    SCREEN = (AppiumBy.ACCESSIBILITY_ID, "ProductDetails-screen")
    # Price label. The name label above it has no accessibility identifier.
    PRICE = (AppiumBy.ACCESSIBILITY_ID, "Price")
    ADD_TO_CART = (AppiumBy.ACCESSIBILITY_ID, "AddToCart")
    AMOUNT = (AppiumBy.ACCESSIBILITY_ID, "Amount")

    @staticmethod
    def product_named(name: str) -> Locator:
        return static_text(name)
