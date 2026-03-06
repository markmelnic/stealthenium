from ._js_cache import load_js
from .wrapper import evaluateOnNewDocument
from selenium.webdriver.remote.webdriver import WebDriver


def webgl_vendor_override(
    driver: WebDriver,
    webgl_vendor: str,
    renderer: str,
    **kwargs
) -> None:
    evaluateOnNewDocument(
        driver, load_js("webgl.vendor.js"),
        webgl_vendor,
        renderer,
    )
