import pytest

from data.catalog import BACKPACK_BLACK


@pytest.mark.cart
@pytest.mark.regression
def test_add_to_cart_updates_badge(catalog, product, cart):
    # Step 1: Open a product from the catalog.
    catalog.wait_until_loaded()
    catalog.open_product(BACKPACK_BLACK)
    product.wait_until_loaded()
    # Step 2: Add one item. The cart tab badge shows the count.
    product.add_to_cart()
    assert product.cart_badge() == "1"
    # Step 3: The cart screen counts the same item.
    product.open_cart()
    cart.wait_until_loaded()
    assert cart.shows_item_count(1) == "1 Items"
