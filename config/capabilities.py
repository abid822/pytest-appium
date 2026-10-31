from appium.options.android import UiAutomator2Options
from appium.options.common.base import AppiumOptions
from appium.options.ios import XCUITestOptions

from config.settings import Settings


def build_options(settings: Settings) -> AppiumOptions:
    """Session capabilities for the platform selected in config.

    iOS is the suite that ships today. Android builds a UiAutomator2 session
    from the same env vars so a later suite can switch PLATFORM=android.
    """
    if settings.platform == "android":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = settings.device_name
        options.app = settings.app_path
        options.no_reset = settings.no_reset
        options.full_reset = False
        options.new_command_timeout = 120
        options.auto_grant_permissions = True
        if settings.platform_version:
            options.platform_version = settings.platform_version
        if settings.udid:
            options.udid = settings.udid
        if settings.app_package:
            options.app_package = settings.app_package
        if settings.app_activity:
            options.app_activity = settings.app_activity
        return options

    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.automation_name = "XCUITest"
    options.device_name = settings.device_name
    options.platform_version = settings.platform_version
    options.app = settings.app_path
    options.bundle_id = settings.bundle_id
    options.no_reset = settings.no_reset
    options.full_reset = False
    options.new_command_timeout = 120
    options.auto_accept_alerts = False
    options.auto_dismiss_alerts = False
    options.should_terminate_app = True
    options.force_app_launch = True
    if settings.udid:
        options.udid = settings.udid
    return options
