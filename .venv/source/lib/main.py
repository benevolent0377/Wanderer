# imports
from . import IO
from . import setup
import sys
from . import extra

def run():
    setup.run()

    if len(sys.argv) < 2:
        print()
        quitKill()
    else:
        print()

# the quit function
def quitKill(preserve=False):
    if not preserve:
        setup.clearCache()

    sys.exit()

