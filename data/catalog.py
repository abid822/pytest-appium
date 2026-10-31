"""English catalog copy from My Demo App en.lproj and Utils.swift.

Prices are stored as strings. The catalog sorts price with a string compare,
so "15.99" comes before "7.99".
"""

BACKPACK_BLACK = "Sauce Labs Backpack - Black"
BACKPACK_BLACK_PRICE = "29.99"
BOLT_BLACK = "Sauce Labs Bolt T-Shirt - Black"
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
