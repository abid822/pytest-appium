from appium.webdriver.common.appiumby import AppiumBy

from config.settings import settings

Locator = tuple[str, str]


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def button(title: str) -> Locator:
    """A button identified by its visible title."""
    escaped = _escape(title)
    if settings.platform == "android":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{escaped}")')
    return (
        AppiumBy.IOS_PREDICATE,
        f'type == "XCUIElementTypeButton" AND (name == "{escaped}" OR label == "{escaped}")',
    )


def static_text(label: str) -> Locator:
    """A static text identified by its visible label."""
    escaped = _escape(label)
    if settings.platform == "android":
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{escaped}")')
    return (
        AppiumBy.IOS_PREDICATE,
        f'type == "XCUIElementTypeStaticText" AND (name == "{escaped}" OR label == "{escaped}")',
    )


def text_field() -> Locator:
    if settings.platform == "android":
        return (AppiumBy.CLASS_NAME, "android.widget.EditText")
    return (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')


def secure_field() -> Locator:
    if settings.platform == "android":
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText")',
        )
    return (AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSecureTextField"')
