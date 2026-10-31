from appium.webdriver.common.appiumby import AppiumBy

from config.settings import settings
from locators.queries import Locator, button, static_text


class CatalogLocators:
    """Catalog screen. Ids are from TabBar.storyboard unless noted."""

    # Accessibility identifier on the catalog root view.
    SCREEN = (AppiumBy.ACCESSIBILITY_ID, "Catalog-screen")
    # "Products" title. The storyboard identifier is "title".
    TITLE = (AppiumBy.ACCESSIBILITY_ID, "title")
    # Cell container. The name label inside uses identifier "Product Name"
    # and its accessibility label is set to the product name at runtime.
    PRODUCT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "ProductItem")
    PRODUCT_NAME = (AppiumBy.ACCESSIBILITY_ID, "Product Name")
    PRODUCT_PRICE = (AppiumBy.ACCESSIBILITY_ID, "Product Price")
    CATALOG_TAB = (AppiumBy.ACCESSIBILITY_ID, "Catalog-tab-item")
    # Sort control has no accessibility identifier. Its storyboard title is "Button".
    # Scope it to the catalog so menu chevrons, which use the same title, are not hit.
    SORT_BUTTON = (
        (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Button")',
        )
        if settings.platform == "android"
        else (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeOther[`name == "Catalog-screen"`]'
            '/**/XCUIElementTypeButton[`name == "Button"`]',
        )
    )

    @staticmethod
    def product_named(name: str) -> Locator:
        return static_text(name)

    @staticmethod
    def sort_option(title: str) -> Locator:
        # Popup titles: "Name - Ascending", "Name - Descending",
        # "Price - Ascending", "Price - Descending".
        return button(title)
