from locators.cart_locators import CartLocators
from screens.base_screen import BaseScreen


class CartScreen(BaseScreen):
    """Cart tab. Empty state uses Go Shopping; a filled cart shows the item count."""

    def wait_until_loaded(self) -> None:
        self.find_visible(CartLocators.SCREEN)

    def shows_item_count(self, count: int) -> str:
        return self.visible_text(CartLocators.items_count(count))
