# a file of local input functions
import os.path
from . import syntax, log
import yaml


# simply prints the string output or creates a query in the terminal, also returns the inputted values
def say(output="", isQuestion=False, isLoop=False, syntaxChk=False, synType="", end="\n", ):
    # checking if the program wants a response, aka: question = yes
    if isQuestion:

        # seeing if the program wants to ask multiple queries
        # if isLoop, then the output value should be an array and not a string
        if isLoop:
            loopVector = len(output)
            count = 0
            usrSay = []  # this is the returned list from the keyboard
            while loopVector > count:  # while the # of questions is greater than the responses, ask a question
                usrSay.append(input(output[count])) # store the user's response to the printed question to the end of usrSay

                # send the data to the log file for this instance
                log.log(output[count], "output")
                log.log(usrSay[count], "input")
                count += 1
            # if there is syntax to be checked for, the syntax library will be called and the applicable syntax will be initialized and returned
            if syntaxChk:
                return syntax.adv(usrSay, synType, isLoop)
            # otherwise return the raw output
            else:
                return usrSay
        # if the output is only to be printed once
        else:
            # logging
            log.log(output, "output")
            
            # again checking for syntax and calling the syntax library if it is True
            if syntaxChk:
                response = syntax.adv(input(output), synType, isLoop)  # says the output and returns the prompt
                log.log(response, "input")
                return response
            # otherwise, return the raw output
            else:
                response = input(output)
                log.log(response, "input")
                return response
    # if the program does not want a response, aka: not a question
    else:

        # if the program has multiple statements to print out
        if isLoop:
            count = 0
            loopVector = len(output)
            while loopVector > count:  # while the number of statements is less than the number already stated, speak
                log.log(output[count], "output")
                # say more
                if syntaxChk:
                    print(syntax.adv(output[count], synType), end=end)
                else:
                    print(output[count], end=end)
                count += 1

        # if the program does not want a loop
        else:
            log.log(output, "output")
            if syntaxChk:
                print(syntax.adv(output, synType), end=end)
            else:
                print(output, end=end)


# WRITE TO A YAML FILE
def yamlWrite(value, element, File, isLoop=False):
    # check if there is data prestored in File
    data = yamlRead(File, element, True)
    if data is None:
        data = {}
        if isLoop and len(element) == len(value):
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})
    else:
        if isLoop:
            count = 0
            while len(element) > count:
                data.update({element[count]: value[count]})
                count += 1

        else:
            data.update({element: value})

    with open(File, "w") as file:
        log.log(element, "wfile", File)
        yaml.dump(data, file)


# read from a yaml file
def yamlRead(File, element, update=False, elements=1):
    with open(File, "r") as file:
        data = yaml.safe_load(file)
        log.log(element, "rfile", File)
        if data is None:
            return None

        else:
            if update:
                count = 0
                while elements > count:
                    data.update({element: data[element]})
                    count += 1

                return data
            else:
                return data[element]


def mkFile(File):
    with open(File, "x") as file:
        log.log(File, "mkfile")
        return os.path.isfile(File)

def mkDir(dir):
    os.mkdir(dir)
    log.log(dir, "mkdir")
    return os.path.isdir(dir)


def fileWrite(value, File, isLoop=False, overwrite=False, update=False, isLog=False):
    if overwrite and not update:
        if isLoop:
            count = 0
            with open(File, "w") as file:
                while len(value) > count:
                    file.write(value[count] + "\n")
                    if not isLog:
                        log.log(value[count], "wfile", File)
                    count += 1
        else:
            with open(File, "w") as file:
                file.write(value)
    elif not overwrite and not update:
        if isLoop:
            count = 0
            with open(File, "a") as file:
                while len(value) > count:
                    file.write(value[count] + "\n")
                    if not isLog:
                        log.log(value[count], "wfile", File)
                    count += 1
        else:
            with open(File, "a") as file:
                file.write(value)
                if not isLog:
                    log.log(value, "wfile", File)

    if update:
        print()

def rmFile(File):
    try:
        os.remove(File)
        return True
    except:
        return False


# reads a file and outputs an array
def fileRead(File):
    with open(File, "r") as file:
        out = []
        for line in file:
            out.append(line)

    log.log(File, "rfile")
    return out
