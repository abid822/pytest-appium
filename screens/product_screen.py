from locators.cart_locators import CartLocators
from locators.product_locators import ProductLocators
from screens.base_screen import BaseScreen


class ProductScreen(BaseScreen):
    """Product detail reached from a catalog cell."""

    def wait_until_loaded(self) -> None:
        self.find_visible(ProductLocators.SCREEN)

    def shows_name(self, name: str) -> str:
        return self.visible_text(ProductLocators.product_named(name))

    def price(self) -> str:
        return self.visible_text(ProductLocators.PRICE)

    def add_to_cart(self) -> None:
        self.tap(ProductLocators.ADD_TO_CART)

    def cart_badge(self) -> str:
        return self.tab_badge(CartLocators.TAB)

    def open_cart(self) -> None:
        self.tap(CartLocators.TAB)
