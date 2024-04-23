from . import IO
from . import system
from . import log
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

def read(pData):
    varsIn = {}
    for item in pData:
        IO.say(item)
        varsIn.update({item['secondaryName'].replace("--", ""): ""})
        varsIn.update({item['secondaryName'].replace("--", ""): item["args"]})

    IO.say(pData)
    if varsIn.__contains__("help"):
        IO.say("hi")
    else:
        IO.say("hello")


