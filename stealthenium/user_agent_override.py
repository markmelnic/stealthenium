from .cdp import execute_cdp_cmd

from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver


def user_agent_override(
        driver: WebDriver,
        user_agent: Optional[str] = None,
        language: Optional[str] = None,
        platform: Optional[str] = None,
        **kwargs
) -> None:
    if user_agent is None:
        ua = execute_cdp_cmd(driver, "Browser.getVersion", {})['userAgent']
    else:
        ua = user_agent
    ua = ua.replace("HeadlessChrome", "Chrome")  # hide headless nature
    override = {"userAgent": ua}
    if language:
        override["acceptLanguage"] = language
    if platform:
        override["platform"] = platform

    execute_cdp_cmd(driver, 'Network.setUserAgentOverride', override)
