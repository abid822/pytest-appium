import base64
from pathlib import Path

import allure
import pytest
from appium import webdriver
from selenium.common.exceptions import WebDriverException

from config.capabilities import build_options
from config.settings import ROOT, settings
from screens.cart_screen import CartScreen
from screens.catalog_screen import CatalogScreen
from screens.login_screen import LoginScreen
from screens.product_screen import ProductScreen
from utils.friendly_report import (
    ReportCollector,
    TestRecord,
    human_title,
    marker_labels,
    readable_error,
    steps_from_item,
    story_why,
    write_report,
)


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


def pytest_configure(config):
    (ROOT / "reports").mkdir(exist_ok=True)
    config._friendly_report = ReportCollector()


def _failure_png(item) -> bytes | None:
    session = getattr(item, "driver", None)
    if session is None:
        return None
    try:
        return session.get_screenshot_as_png()
    except WebDriverException:
        return None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    screenshot_b64 = ""
    if report.failed and report.when in {"setup", "call"}:
        png = _failure_png(item)
        if png:
            screenshot_b64 = base64.b64encode(png).decode()
            allure.attach(
                png,
                name="failure",
                attachment_type=allure.attachment_type.PNG,
            )

    if report.when == "teardown" or (report.when == "setup" and not report.failed):
        return
    collector = getattr(item.config, "_friendly_report", None)
    if collector is None:
        return
    file_name = Path(str(item.path)).name if getattr(item, "path", None) else ""
    record = TestRecord(
        nodeid=item.nodeid,
        name=item.name,
        title=human_title(item.name),
        why=story_why(item),
        steps=steps_from_item(item),
        markers=marker_labels(item),
        outcome=report.outcome,
        duration_s=report.duration or 0.0,
        stdout=getattr(report, "capstdout", "") or "",
        error=readable_error(report.longrepr) if report.failed else "",
        screenshot_b64=screenshot_b64,
        file_name=file_name,
    )
    if report.when == "call":
        collector.upsert_call(record)
    else:
        collector.add(record)


def pytest_sessionfinish(session, exitstatus):
    collector = getattr(session.config, "_friendly_report", None)
    if collector is None:
        return
    write_report(collector, ROOT / "reports" / "report.html")
