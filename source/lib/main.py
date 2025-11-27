from source.core import system, cmd, IO
import sys
from . import banner, files, args
from source.update import Ucore as core
from source.update import Ulib as lib

def run():

 #   core.get()

    system.init(["config", "data", "log", "/tmp", "ex", "downloads"], [], True)

  #  files.mkConfig()

    lib.get("wanderer")

    if len(sys.argv) >= 2:  # if command arguments are given
        banner.out()
        system.dumpHead()
        args.parse(cmd.parse(sys.argv[1:]))
        system.quitKill()
    else:  # if no command arguments were given
        banner.out()
        system.dumpHead()
        loop = True
        while loop:

            respon = IO.say(["Enter the desired website. ", "Enter tags, accounts, profiles, or direct links. ",
                             "Enter your desired save directory. "], isLoop=True, isQuestion=True, syntaxChk=True,
                            synType="internal")

            commands = {"host": respon[0], "attributes": respon[1], "stor": respon[2]}
            print(commands)

            args.parse(commands, 1, ["host", "attributes", "stor"])

            repeat = IO.say("Download something else?", True, syntaxChk=True, synType="internal")
            if repeat.__eq__("yes") or repeat.__eq__("y") or repeat.__eq__("1"):
                print()
            else:
                loop = False

        # close the program
        system.quitKill()
