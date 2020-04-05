# default call: 
# python .make/set_name.py waymo

# reverse operation: 
# python .make/set_name.py PKG_NAME waymo

import os
import sys
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("target_name", type=str) #, nargs="?", default=Path(os.getcwd()).name)
parser.add_argument("source_name", type=str, nargs="?", default="PKG_NAME")
args = parser.parse_args(sys.argv[1:])

source_name = args.source_name
target_name = args.target_name

Path(source_name).replace(target_name)

files_with_placeholder =[
    Path("Dockerfile"),
    Path("Pipfile"),
    Path("setup.py"),
    Path(target_name, "__main__.py"),
    Path(target_name, "app.py"),
    Path(target_name, "conf.py"),
]


for p in files_with_placeholder: 
    p.write_text(
        p.read_text().replace(
            source_name, 
            target_name))
    
