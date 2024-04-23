# imports
from . import log
from . import system
import sys
from . import IO
from . import cmd

def run():
    system.init()

    if len(sys.argv) >= 2:  # if command arguments are given

        system.dumpHead()
        cmd.parse(sys.argv[1:])
        quitKill()
    else:  # if no command arguments were given
        system.dumpHead()
        quitKill()

# the quit function
def quitKill(preserve=False):
    if not preserve:
        system.clearCache()
    log.log("", "quit")
    sys.exit()

