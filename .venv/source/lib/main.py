# imports
from . import log
from . import system
import sys
from . import IO
from . import extra

def run():
    system.init()

    if len(sys.argv) < 2:
        quitKill()
    else:
        print()

# the quit function
def quitKill(preserve=False):
    if not preserve:
        system.clearCache()

    log.log("", "quit")
    sys.exit()

