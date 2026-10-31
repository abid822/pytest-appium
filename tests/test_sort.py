import pytest

from data.catalog import BOLT_BLACK, SHIRT_YELLOW


@pytest.mark.sort
@pytest.mark.regression
def test_sort_products(catalog):
    # Step 1: Name descending puts the last alphabetical product first.
    catalog.wait_until_loaded()
    catalog.sort_by("Name - Descending")
    catalog.wait_for_product(SHIRT_YELLOW)
    assert catalog.product_names()[0] == SHIRT_YELLOW
    # Step 2: Price uses a string compare, so 15.99 (the bolt shirt) is first.
    catalog.sort_by("Price - Ascending")
    catalog.wait_for_product(BOLT_BLACK)
    assert catalog.product_names()[0] == BOLT_BLACK
