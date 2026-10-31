import pytest

from data.catalog import BIKE_LIGHT, SHIRT_YELLOW


@pytest.mark.sort
@pytest.mark.regression
def test_sort_products(catalog):
    # Step 1: Name descending puts the last alphabetical product first.
    catalog.wait_until_loaded()
    catalog.sort_by("Name - Descending")
    catalog.wait_for_product(SHIRT_YELLOW)
    assert catalog.product_names()[0] == SHIRT_YELLOW
    # Step 2: Price is a stable string compare. 15.99 stays in front, so the
    # yellow shirt remains first. "9.99" sorts last, so the bike light is at the bottom.
    catalog.sort_by("Price - Ascending")
    catalog.wait_for_product(SHIRT_YELLOW)
    assert catalog.product_names()[0] == SHIRT_YELLOW
    assert catalog.product_names_at_bottom()[-1] == BIKE_LIGHT
