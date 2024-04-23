from . import IO
from . import system
from . import log
from . import helper
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
                    if loopVectorA+1 < len(values):
                        if values[loopVectorA+1].startswith("-"):
                            IO.say(f"{values[loopVectorA+1]} is not a valid option for {command['name']}")
                            log.log(f"{values[loopVectorA+1]} is not a valid option for {command['name']}", "err")
                            loopVectorA += 1
                        else:
                            if values[loopVectorA+1].find(",") != -1:
                                command.update({"args": values[loopVectorA + 1].split(",")})
                                cmds.append(command)
                            else:
                                command.update({"args": values[loopVectorA+1]})
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

        if varsIn.__contains__("help"):
            helper.request(varsIn.__getattribute__("help"))

        else:
            # add custon syntax or regex checks for each of the command's arguments before passing them, they have only been stripped and lowercased for internal processing ease
            if not varsIn.__contains__("host"):
                IO.say("You must define a hostname with '-h' or '--host'.")
                log.log("No hostname defined.", "err")
            if not varsIn.__contains__("attributes"):
                IO.say("You must provide attributes: links, tags, pages, etc... Define these with '-A' or '--attributes'.")
                log.log("No attributes provided.", "err")
            if not varsIn.__contains__("stor"):
                IO.say(f"Storing files in {system.getCWD()}downloads{system.getSlash()}.")
            if not varsIn.__contains__("timeout"):
                IO.say("Default timeout is 45 seconds. Use '-t' or '--timeout' to alter.")
                varsIn.update({"timeout": 45})

    else:
        print()




