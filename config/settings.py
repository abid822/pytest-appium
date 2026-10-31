import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

_PLATFORMS = ("ios", "android")


def _bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _platform() -> str:
    raw = (os.getenv("PLATFORM") or "ios").strip().lower()
    if raw not in _PLATFORMS:
        allowed = ", ".join(_PLATFORMS)
        raise ValueError(f"PLATFORM must be one of {allowed} (got {raw!r}).")
    return raw


PLATFORM = _platform()


class Settings:
    platform: str = PLATFORM
    appium_url: str = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
    app_path: str = os.getenv(
        "APP_PATH",
        "/Users/abid/mobile-testing/apps/Payload/My Demo App.app",
    )
    device_name: str = os.getenv(
        "DEVICE_NAME",
        "iPhone 18 Pro" if PLATFORM == "ios" else "Android Emulator",
    )
    platform_version: str = os.getenv(
        "PLATFORM_VERSION",
        "27.0" if PLATFORM == "ios" else "",
    )
    udid: str = os.getenv("UDID", "").strip()
    bundle_id: str = os.getenv("BUNDLE_ID", "com.saucelabs.mydemo.app.ios")
    app_package: str = os.getenv("APP_PACKAGE", "com.saucelabs.mydemoapp.android")
    app_activity: str = os.getenv("APP_ACTIVITY", "").strip()
    explicit_wait_seconds: int = int(os.getenv("EXPLICIT_WAIT_SECONDS", "15"))
    no_reset: bool = _bool("NO_RESET", True)
    demo_username: str = os.getenv("DEMO_USERNAME", "bod@example.com")
    demo_password: str = os.getenv("DEMO_PASSWORD", "10203040")


settings = Settings()
