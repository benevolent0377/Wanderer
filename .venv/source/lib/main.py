# imports
from . import IO
from . import setup
import sys


def run():
    setup.run()

    if len(sys.argv) < 2:
        IO.yamlWrite("calithos", "author", f"{setup.getCWD()}{setup.getSlash()}config{setup.getSlash()}config.yaml", update=True)
        print()
    else:
        print()
