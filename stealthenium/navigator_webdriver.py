from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def navigator_webdriver(driver: WebDriver, **kwargs) -> None:
    evaluateOnNewDocument(driver, load_js("navigator.webdriver.js"))
