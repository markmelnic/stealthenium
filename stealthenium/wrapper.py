from .cdp import execute_cdp_cmd

import json
from selenium.webdriver import Chrome as Driver
from typing import Any

def evaluationString(fun: str, *args: Any) -> str:
    """Convert function and arguments to str."""
    _args = ', '.join([
        json.dumps('undefined' if arg is None else arg) for arg in args
    ])
    expr = '(' + fun + ')(' + _args + ')'
    return expr


def evaluateOnNewDocument(driver: Driver, pagefunction: str, *args: str) -> None:

    js_code = evaluationString(pagefunction, *args)

    execute_cdp_cmd(driver, "Page.addScriptToEvaluateOnNewDocument", {
        "source": js_code,
    })
