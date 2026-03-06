from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def navigator_vendor(driver: WebDriver, vendor: str, **kwargs) -> None:
    evaluateOnNewDocument(driver, load_js("navigator.vendor.js"), vendor)
