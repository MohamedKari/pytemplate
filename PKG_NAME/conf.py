import os
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("name", type=str)
args = parser.parse_args(sys.argv[1:])

print(args.name)

