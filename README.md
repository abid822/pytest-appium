# pytest-appium

Pytest and Appium framework for the Sauce Labs My Demo App on iOS.

The app under test is the native iOS build, bundle id `com.saucelabs.mydemo.app.ios`. Source and releases: [saucelabs/my-demo-app-ios](https://github.com/saucelabs/my-demo-app-ios).

Locators live next to the screens that use them. Screens share a `BaseScreen`. Tests talk to screens, not to raw driver calls. `PLATFORM` in the environment selects iOS or Android when the session is created.

## Requirements

Runs locally on an Apple Silicon Mac:

- Python 3.12
- Xcode 27.2
- iPhone 18 Pro simulator on iOS 27.0
- Appium 3.9.0
- XCUITest driver 12.22.8
- App binary at `/Users/abid/mobile-testing/apps/Payload/My Demo App.app`

## Setup

Create a virtualenv and install the Python packages:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Open the folder in Cursor, install the recommended Python extension, and select the `.venv` interpreter. Cmd+click a function (F12) jumps to its definition. Ctrl+- goes back.

Install Appium and the XCUITest driver, then confirm the driver is present:

```bash
npm install -g appium@3.9.0
appium driver install xcuitest@12.22.8
appium driver list --installed
```

Select the Xcode 27.2 install when more than one copy is on the machine:

```bash
sudo xcode-select -s /Applications/Xcode.app
```

Boot the simulator:

```bash
xcrun simctl boot "iPhone 18 Pro"
open -a Simulator
```

Appium can boot the simulator named by `DEVICE_NAME` if it is not already running. Leave `UDID` empty unless a specific simulator should be targeted.

Start the Appium server in another terminal:

```bash
appium
```

The server listens on `http://127.0.0.1:4723` unless `APPIUM_URL` says otherwise.

## Configuration

Values come from the environment. A `.env` file in the project root is loaded first. See `.env.example`.

| Variable | Default | Role |
| --- | --- | --- |
| `PLATFORM` | `ios` | `ios` or `android` |
| `APPIUM_URL` | `http://127.0.0.1:4723` | Appium server |
| `APP_PATH` | `/Users/abid/mobile-testing/apps/Payload/My Demo App.app` | Simulator `.app` or Android `.apk` |
| `DEVICE_NAME` | `iPhone 18 Pro` | Simulator or emulator name |
| `PLATFORM_VERSION` | `27.0` | OS version |
| `UDID` | empty | Optional device id |
| `BUNDLE_ID` | `com.saucelabs.mydemo.app.ios` | iOS bundle id |
| `APP_PACKAGE` | `com.saucelabs.mydemoapp.android` | Android package when `PLATFORM=android` |
| `APP_ACTIVITY` | empty | Optional Android activity |
| `EXPLICIT_WAIT_SECONDS` | `15` | Wait for screen elements |
| `NO_RESET` | `true` | Keep the installed app between sessions |
| `DEMO_USERNAME` | `bod@example.com` | Username used by the login test |
| `DEMO_PASSWORD` | `10203040` | Password used by the login test |

`PLATFORM=android` builds a UiAutomator2 session from the same variables (`APP_PATH` should point at an APK, and `DEVICE_NAME` at an emulator or device). The locators in this repo are the iOS accessibility ids. Android screen locators are not filled in yet.

## Running tests

```bash
pytest
pytest -m smoke
pytest -m regression
pytest tests/test_catalog.py
```

Each test opens its own Appium session and closes it at the end. Markers are `smoke` and `regression`, plus `catalog`, `cart`, `login`, and `sort`.

## Allure report

Failed tests attach a PNG to the Allure result. Results are written to `allure-results/`. Install the Allure command line and open the report:

```bash
brew install allure
allure serve allure-results
```

## Tests

- Catalog loads with products. The app sorts by name ascending on launch, so Sauce Labs Backpack - Black is first.
- Opening that product shows its name and price (`$ 29.99`).
- Add to cart reveals the cart-tab badge `1`. The cart screen then shows `1 Items`.
- Login from the More tab with `DEMO_USERNAME` / `DEMO_PASSWORD` returns to the catalog. The login screen also lists `bob@example.com`, `alice@example.com`, `john@example.com`, and `visual@example.com`. Tapping one of those fills the password `10203040`. The iOS login screen accepts any non-empty username and password.
- Submitting the login form with both fields empty shows `Validation Error!` and `Username is required`.
- Sort by name descending, then by price ascending. The app compares prices as strings, so `15.99` sorts before `7.99`.

## Project structure

```
.
├── .env.example
├── .github/workflows/lint.yml
├── .gitignore
├── config/
│   ├── __init__.py
│   ├── capabilities.py
│   └── settings.py
├── conftest.py
├── data/
│   ├── __init__.py
│   └── catalog.py
├── locators/
│   ├── __init__.py
│   ├── cart_locators.py
│   ├── catalog_locators.py
│   ├── login_locators.py
│   ├── menu_locators.py
│   ├── product_locators.py
│   └── queries.py
├── screens/
│   ├── __init__.py
│   ├── base_screen.py
│   ├── cart_screen.py
│   ├── catalog_screen.py
│   ├── login_screen.py
│   └── product_screen.py
├── tests/
│   ├── test_cart.py
│   ├── test_catalog.py
│   ├── test_login.py
│   ├── test_product.py
│   └── test_sort.py
├── pytest.ini
├── README.md
├── requirements.txt
└── ruff.toml
```

## Continuous integration

`.github/workflows/lint.yml` installs the Python dependencies, runs `ruff check`, and runs `pytest --collect-only`. It does not boot a simulator or start Appium. Execute the tests on a Mac with the simulator above.

## Locators

Accessibility ids were taken from the My Demo App storyboards:

- `Catalog-screen`, `title`, `ProductItem`, `Product Name`, `Product Price`
- `ProductDetails-screen`, `Price`, `AddToCart`, `Amount`
- `Cart-screen`, `Cart-tab-item`, `Catalog-tab-item`, `More-tab-item`
- `Login Button`, `LogOut-menu-item`

The username field, password field, sort button, and cart badge have no accessibility id. Those locators use the field type, the sort button title inside `Catalog-screen`, or the label next to `Cart-tab-item`.
