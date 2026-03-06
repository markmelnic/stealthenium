from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def chrome_runtime(driver: WebDriver, run_on_insecure_origins: bool = False, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, load_js("chrome.runtime.js"),
        run_on_insecure_origins,
    )
