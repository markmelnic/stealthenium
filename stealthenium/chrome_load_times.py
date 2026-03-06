from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def chrome_load_times(driver: WebDriver, **kwargs) -> None:
    evaluateOnNewDocument(driver, load_js("chrome.loadTimes.js"))
