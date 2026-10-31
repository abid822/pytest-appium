from appium.webdriver.common.appiumby import AppiumBy


class MenuLocators:
    """More menu. Ids are from Menu.storyboard."""

    MORE_TAB = (AppiumBy.ACCESSIBILITY_ID, "More-tab-item")
    LOGIN = (AppiumBy.ACCESSIBILITY_ID, "Login Button")
    LOGOUT_ROW = (AppiumBy.ACCESSIBILITY_ID, "LogOut-menu-item")
    WEBVIEW = (AppiumBy.ACCESSIBILITY_ID, "Webview-menu-item")
    ABOUT = (AppiumBy.ACCESSIBILITY_ID, "About-menu-item")
    RESET_APP = (AppiumBy.ACCESSIBILITY_ID, "ResetAppState-menu-item")
