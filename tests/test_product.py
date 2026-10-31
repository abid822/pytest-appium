import pytest

from data.catalog import BACKPACK_BLACK, BACKPACK_BLACK_PRICE, price_label


@pytest.mark.catalog
@pytest.mark.smoke
@pytest.mark.regression
def test_product_detail_shows_name_and_price(catalog, product):
    # Step 1: Open the first product in the default sort.
    catalog.wait_until_loaded()
    catalog.open_product(BACKPACK_BLACK)
    # Step 2: Detail shows that product's name and price.
    product.wait_until_loaded()
    assert product.shows_name(BACKPACK_BLACK) == BACKPACK_BLACK
    assert product.price() == price_label(BACKPACK_BLACK_PRICE)
