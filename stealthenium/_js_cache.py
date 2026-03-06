from functools import lru_cache
from pathlib import Path

_JS_DIR = Path(__file__).parent / "js"


@lru_cache(maxsize=None)
def load_js(filename: str) -> str:
    return (_JS_DIR / filename).read_text()
