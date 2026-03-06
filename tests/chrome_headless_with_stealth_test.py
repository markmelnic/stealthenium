import os
import math
import base64
import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from stealthenium import stealth


@pytest.fixture
def browser_data():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    test_html = Path(__file__).parent / "static" / "test.html"
    url = test_html.as_uri()
    driver.get(url)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".passed, .failed-text"))
    )

    metrics = driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
    width = math.ceil(metrics['contentSize']['width'])
    height = math.ceil(metrics['contentSize']['height'])
    screen_orientation = dict(angle=0, type='portraitPrimary')
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        'mobile': False,
        'width': width,
        'height': height,
        'deviceScaleFactor': 1,
        'screenOrientation': screen_orientation,
    })
    clip = dict(x=0, y=0, width=width, height=height, scale=1)
    opt = {'format': 'png', 'clip': clip}

    result = driver.execute_cdp_cmd('Page.captureScreenshot', opt)
    html = driver.page_source
    driver.quit()
    return html, result


def test_stealth_png(browser_data):
    _, result = browser_data
    buffer = base64.b64decode(result.get('data', b''))
    # PNG files start with an 8-byte signature
    assert buffer[:8] == b'\x89PNG\r\n\x1a\n'


def test_stealth_failed(browser_data):
    html, _ = browser_data
    assert "failed-text" not in html and "passed" in html


def test_stealth_warn(browser_data):
    html, _ = browser_data
    assert "warn" not in html and "passed" in html
