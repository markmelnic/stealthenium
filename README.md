# stealthenium ![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)

A python package to prevent selenium detection. This programme is trying to make python selenium more stealthy. As of now August 2024 stealthenium **only** supports Chrome and Remote WebDriver.

This is a fork of [selenium-stealth ](https://github.com/diprajpatra/selenium-stealth) developed by [@diprajpatra](https://github.com/diprajpatra) and has came to be because it is no longer maintained (last commit November 5 2020 as of August 23 2024). It can be seen as a re-implementation of JavaScript [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth) developed by [@berstend](https://github.com/berstend).

## Features

- **passes all public bot tests.**

- **bypass Cloudflare and other bot detection systems.**

- **maintains reasonable reCAPTCHA v3 score**

## Install

stealthenium is available on PyPI you can install with pip.

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

## Test results (red - bad)

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

Copyright © 2024, [markmelnic](https://github.com/markmelnic/stealthenium). Released under the MIT License.
