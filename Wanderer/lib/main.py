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
        loop = True
        while loop:

            respon = IO.say(["Enter the desired website. ", "Enter tags, accounts, profiles, or direct links. ",
                             "Enter your desired save directory. "], isLoop=True, isQuestion=True, syntaxChk=True,
                            synType="internal")

            commands = {"host": respon[0], "attributes": respon[1], "stor": respon[2]}

            cmd.read(commands, 1)

            repeat = IO.say("Download something else?", True, syntaxChk=True, synType="internal")
            IO.say(repeat)
            if repeat.__eq__("yes") or repeat.__eq__("y") or repeat.__eq__("1"):
                print()
            else:
                loop = False


        # close the program
        quitKill()


# the quit function
def quitKill(preserve=False):
    if not preserve:
        system.clearCache()
    log.log("", "quit")
    sys.exit()
