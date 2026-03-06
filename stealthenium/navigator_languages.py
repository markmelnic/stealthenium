from typing import List

from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def navigator_languages(driver: WebDriver, languages: List[str], **kwargs) -> None:
    evaluateOnNewDocument(
        driver, load_js("navigator.languages.js"),
        languages,
    )
