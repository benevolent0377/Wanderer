from source.core import system, cmd, IO
import sys
from . import banner, files


def run():
    system.init(["config", "data", "log", "/tmp", "ex", "downloads"], [])
    files.mkConfig()

    if len(sys.argv) >= 2:  # if command arguments are given
        banner.out()
        system.dumpHead()
        cmd.parse(sys.argv[1:])
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

            cmd.read(commands, ["host", "attributes", "stor"], 1, "host",
                     "(http(s)?:\\/\\/)?([a-z0-9]){3,256}\\.([a-z0-9]){2,6}$")

            repeat = IO.say("Download something else?", True, syntaxChk=True, synType="internal")
            if repeat.__eq__("yes") or repeat.__eq__("y") or repeat.__eq__("1"):
                print()
            else:
                loop = False

        # close the program
        system.quitKill()
