# Stealthenium ![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)

**Stealthenium** is a Python package designed to prevent Selenium from being detected. Its primary goal is to enhance Selenium’s stealth capabilities ensuring smooth automation while bypassing detection systems. Currently, Stealthenium only supports **Chrome** and **Remote WebDriver**.

This project is a fork of the now-unmaintained [selenium-stealth](https://github.com/diprajpatra/selenium-stealth) by [diprajpatra](https://github.com/diprajpatra), last updated on November 5 2020 as of August 23 2024. It serves as a Python equivalent of the JavaScript [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth) developed by [berstend](https://github.com/berstend).

## Features

- **Passes public bot detection tests.**
- **Bypasses Cloudflare and other bot detection systems.**
- **Maintains a reasonable reCAPTCHA v3 score.**

## Installation

Stealthenium is available on PyPI. Install it via pip:

```
$ pip install stealthenium
```

## Usage

```python
from selenium import webdriver
from stealthenium import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(
    options=options,
    service=webdriver.ChromeService(r"\chromedriver.exe")
)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://bot.sannysoft.com/"
driver.get(url)
time.sleep(5)
driver.quit()
```

## Args

```python
stealth(
    driver: Driver,
    user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    languages: [str] = ["en-US", "en"],
    vendor: str = "Google Inc.",
    platform: str = "Win32",
    webgl_vendor: str = "Intel Inc.",
    renderer: str = "Intel Iris OpenGL Engine",
    fix_hairline: bool = False,
    run_on_insecure_origins: bool = False,
)
```

## Test results (red = bad)

Without <strong>stealthenium</strong>

<table class="image">
<tr>
  <td><figure class="image"><a href="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headless_without_stealth.png"><img src="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headless_without_stealth.png"></a><figcaption>headless</figcaption></figure></td>
  <td><figure class="image"><a href="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headful_without_stealth.png"><img src="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headful_without_stealth.png"></a><figcaption>headful</figcaption></figure></td>
</tr>
</table>

With <strong>stealthenium</strong>

<table class="image">
<tr>
  <td><figure class="image"><a href="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headless_with_stealth.png"><img src="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headless_with_stealth.png"></a><figcaption>headless</figcaption></figure></td>
  <td><figure class="image"><a href="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headful_with_stealth.png"><img src="https://raw.githubusercontent.com/markmelnic/stealthenium/main/stealthtests/selenium_chrome_headful_with_stealth.png"></a><figcaption>headful</figcaption></figure></td>
</tr>
</table>

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/markmelnic/stealthenium/blob/main/LICENSE) file for details.

© 2024 [markmelnic](https://github.com/markmelnic)
