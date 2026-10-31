from selenium.common.exceptions import WebDriverException

from locators.cart_locators import CartLocators
from locators.catalog_locators import CatalogLocators
from locators.menu_locators import MenuLocators
from screens.base_screen import BaseScreen


class CatalogScreen(BaseScreen):
    """Product grid shown when the app launches."""

    def wait_until_loaded(self) -> None:
        # Catalog root and the Products title.
        self.find_visible(CatalogLocators.SCREEN)
        self.find_visible(CatalogLocators.TITLE)

    def title(self) -> str:
        return self.visible_text(CatalogLocators.TITLE)

    def product_names(self) -> list[str]:
        return self.visible_texts(CatalogLocators.PRODUCT_NAME)

    def open_product(self, name: str) -> None:
        # Step 1: Tap the product name on the grid.
        self.tap(CatalogLocators.product_named(name))

    def wait_for_product(self, name: str) -> None:
        self.find_visible(CatalogLocators.product_named(name))

    def open_sort(self) -> None:
        self.tap(CatalogLocators.SORT_BUTTON)

    def sort_by(self, option: str) -> None:
        # Step 1: Open the sort sheet.
        self.open_sort()
        # Step 2: Pick a sort option. The sheet closes itself.
        self.tap(CatalogLocators.sort_option(option))

    def open_cart(self) -> None:
        self.tap(CartLocators.TAB)

    def open_more(self) -> None:
        self.tap(MenuLocators.MORE_TAB)

    def product_names_at_bottom(self) -> list[str]:
        # Collection cells that are off screen are not in the tree. Scroll
        # until the visible set stops changing, which is the bottom of the grid.
        previous: list[str] | None = None
        names = self.product_names()
        for _ in range(12):
            if names == previous:
                break
            previous = names
            try:
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
            except WebDriverException:
                break
            names = self.product_names()
        return names

    def cart_badge(self) -> str:
        return self.tab_badge(CartLocators.TAB)
