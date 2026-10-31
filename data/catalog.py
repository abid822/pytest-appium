"""English catalog copy from My Demo App en.lproj and Utils.swift.

Prices are stored as strings. sorted(by:) is stable, and "15.99" sorts before
"29.99", "49.99", "7.99", and "9.99". After name descending, the yellow shirt
stays first. The bike light ("9.99") sorts last.
"""

BACKPACK_BLACK = "Sauce Labs Backpack - Black"
BACKPACK_BLACK_PRICE = "29.99"
BOLT_BLACK = "Sauce Labs Bolt T-Shirt - Black"
BIKE_LIGHT = "Sauce Labs Bike Light"
SHIRT_YELLOW = "Test.allTheThings() T-Shirt - Yellow"

# LoginViewController only rejects an empty username or password.
# These are the accounts drawn on Authentication.storyboard. Tapping one
# fills the password below. Any non-empty pair is accepted.
DEMO_ACCOUNTS = (
    "bob@example.com",
    "alice@example.com",
    "john@example.com",
    "visual@example.com",
)
DEMO_PASSWORD = "10203040"
USERNAME_REQUIRED = "Username is required"
VALIDATION_TITLE = "Validation Error!"


def price_label(amount: str) -> str:
    """ProductPageDetailViewController formats price as "$ " plus the amount."""
    return f"$ {amount}"
