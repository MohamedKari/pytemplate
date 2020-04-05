# terminology: 
# package mode: 
# - executing a module with python -m PKG_NAME (assuming there is __main__.py module)
# - executing a module with python -m PKG_NAME.some_module
# - importing it from a different module
#
# script mode:
# - executing a module with python some_module.py

# RELATIVE IMPORTS: works in package mode
# --
# from . import conf
# from .utils import log

# ABSOLUTE IMPORT relative to the PKG_NAME parent, i. e. imports have a leading "PKG_NAME."
# works in package mode because when invoking python -m PKG_NAME, the current director is added to the path (https://www.python.org/dev/peps/pep-0338/)
# doesn't work in script mode (even with pythin PKG_NAME/app.py), becuase the current directory
# --
# from PKG_NAME import conf
# from PKG_NAME.utils import log

# ABSOLTE IMPORTS and PATH MODIFICATION: relative to the PKG_NAME parent, i. e. imports have a leading "PKG_NAME."
# --
# works in package mode because when invoking python -m PKG_NAME, the current director is added to the path (https://www.python.org/dev/peps/pep-0338/)
# works in script mode and in package mode
import sys, os; sys.path.insert(0, os.getcwd())
from PKG_NAME import conf
from PKG_NAME.utils import log

# entry point to application
def run():
    print("hello from app.py")