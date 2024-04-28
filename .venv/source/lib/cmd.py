from . import IO
from . import system
from . import log
from . import helper
from . import syntax
from . import web


# a file to parse all commands

def parse(values):
    cmdData = IO.yamlRead(f'{system.getConfigPath()}parent.yaml', 'cmdList')
    cmds = []
    loopVectorB = 0
    for command in cmdData:
        loopVectorA = 0
        while len(values) > loopVectorA:
            if command["name"].__eq__(values[loopVectorA]) or command["secondaryName"].__eq__(values[loopVectorA]):
                if command["takesParams"] >= 0:
                    if loopVectorA + 1 < len(values):
                        if values[loopVectorA + 1].startswith("-") and command["takesParams"] != 1:
                            IO.say(f"{values[loopVectorA + 1]} is not a valid option for {command['name']}")
                            log.log(f"{values[loopVectorA + 1]} is not a valid option for {command['name']}", "err")
                            loopVectorA += 1
                        else:
                            if values[loopVectorA + 1].find(",") != -1:
                                command.update({"args": values[loopVectorA + 1].split(",")})
                                cmds.append(command)
                            else:
                                command.update({"args": values[loopVectorA + 1]})
                                cmds.append(command)

                            loopVectorA += 2
                    else:
                        command.update({"args": ""})
                        cmds.append(command)
                        loopVectorA += 1
                else:
                    loopVectorA += 1
            else:
                loopVectorA += 1

        loopVectorB += 1

    read(cmds)


def read(pData, mode=0):
    varsIn = {}

    if mode == 0:

        for item in pData:
            varsIn.update({item['secondaryName'].replace("--", ""): ""})
            varsIn.update({item['secondaryName'].replace("--", ""): item["args"]})
    else:
        varsIn = pData

    if mode == 0:
        IO.say(varsIn)
        if varsIn.__contains__("help"):
            helper.request(varsIn.__getitem__("help"))
        else:
            # add custom syntax or regex checks for each of the command's arguments before passing them, they have only been stripped and lowercased for internal processing ease
            if not varsIn.__contains__("host"):
                IO.say("You must define a hostname with '-H' or '--host'.")
                log.log("No hostname defined.", "err")
            if not varsIn.__contains__("attributes"):
                IO.say(
                    "You must provide attributes: links, tags, pages, etc... Define these with '-A' or '--attributes'.")
                log.log("No attributes provided.", "err")
            if not varsIn.__contains__("stor"):
                IO.say(f"Storing files in {system.getDownloadPath()}")
            if not varsIn.__contains__("timeout"):
                IO.say("Default timeout is 45 seconds. Use '-t' or '--timeout' to alter.")
                varsIn.update({"timeout": "45"})

            if not syntax.adv(varsIn["timeout"], regex=True, regexStr=r"^([0-9]){1,3}$"):
                IO.say("Invalid timeout.")
                varsIn.update({"timeout": "45"})

            if varsIn.__contains__("port"):
                if not syntax.adv(varsIn["port"], regex=True, regexStr=r"^([0-9]){2,5}$"):
                    IO.say(f"Invalid port: {varsIn['port']}")
                    log.log("invalid port", "err")

    else:
        if not syntax.adv(varsIn["host"], regex=True, regexStr=r"(http(s)?:\/\/)?([a-z0-9]){3,256}\.([a-z0-9]){2,6}$"):
            IO.say(f"'{varsIn['host']} is not a valid link.'")

        varsIn.update({"stor": syntax.adv(varsIn["stor"], "dir")})

