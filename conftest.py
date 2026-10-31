import allure
import pytest
from appium import webdriver
from selenium.common.exceptions import WebDriverException

from config.capabilities import build_options
from config.settings import settings
from screens.cart_screen import CartScreen
from screens.catalog_screen import CatalogScreen
from screens.login_screen import LoginScreen
from screens.product_screen import ProductScreen


@pytest.fixture
def driver(request):
    """Appium session for one test. Quit tears the session down."""
    session = webdriver.Remote(
        command_executor=settings.appium_url,
        options=build_options(settings),
    )
    request.node.driver = session
    yield session
    app_id = settings.bundle_id if settings.platform == "ios" else settings.app_package
    try:
        if app_id:
            session.terminate_app(app_id)
    except WebDriverException:
        pass
    session.quit()


@pytest.fixture
def catalog(driver) -> CatalogScreen:
    return CatalogScreen(driver)


@pytest.fixture
def product(driver) -> ProductScreen:
    return ProductScreen(driver)


@pytest.fixture
def cart(driver) -> CartScreen:
    return CartScreen(driver)


@pytest.fixture
def login(driver) -> LoginScreen:
    return LoginScreen(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if not report.failed or report.when not in {"setup", "call"}:
        return
    session = getattr(item, "driver", None)
    if session is None:
        return
    try:
        png = session.get_screenshot_as_png()
    except WebDriverException:
        return
    allure.attach(
        png,
        name="failure",
        attachment_type=allure.attachment_type.PNG,
    )
