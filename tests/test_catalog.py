import pytest

from data.catalog import BACKPACK_BLACK


@pytest.mark.catalog
@pytest.mark.smoke
@pytest.mark.regression
def test_catalog_loads_products(catalog):
    # Step 1: The app opens on the catalog.
    catalog.wait_until_loaded()
    # Step 2: The header is on screen and at least one cell rendered.
    # The storyboard accessibility label on that header is "title"; the visible copy is "Products".
    assert catalog.title() in {"Products", "title"}
    names = catalog.product_names()
    assert names, "Catalog did not render any products"
    # Step 3: Launch sort is name ascending, so the black backpack is first.
    assert names[0] == BACKPACK_BLACK
