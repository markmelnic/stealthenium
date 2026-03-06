from .cdp import execute_cdp_cmd

import json
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any

def evaluationString(fun: str, *args: Any) -> str:
    """Convert function and arguments to str."""
    _args = ', '.join([
        'undefined' if arg is None else json.dumps(arg) for arg in args
    ])
    expr = '(' + fun + ')(' + _args + ')'
    return expr


def evaluateOnNewDocument(driver: WebDriver, pagefunction: str, *args: Any) -> None:

    js_code = evaluationString(pagefunction, *args)

    execute_cdp_cmd(driver, "Page.addScriptToEvaluateOnNewDocument", {
        "source": js_code,
    })
