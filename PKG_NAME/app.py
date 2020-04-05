# run with `python -m PKG_NAME` (exploiting __main__.py) or `python -m PKG_NAME.app`

from . import conf
from .utils import log

# entry point to application
def run():
    print("hello from app.py")