# a file of local inout functions making the process easy and keeping the main file decluttered
from . import syntax
import yaml

# simply prints the string output or creates a query in the terminal, also returns the inputted values
def say(output, isQuestion=False, isLoop=False, syntaxChk=False, synType="", end="\n", ):
    # checking if the program wants a response, aka: question = yes
    if isQuestion:

        # seeing if the program wants to ask multiple queries
        if isLoop:
            loopVector = len(output)
            count = 0
            usrSay = []  # this is the returned list
            while loopVector > count:  # while the # of questions is greater than the responses, ask a question
                usrSay.append(input(output[count]))
                count += 1

            if syntaxChk:
                return syntax.adv(usrSay, synType, isLoop)
            else:
                return usrSay

        else:

            if syntaxChk:
                return syntax.adv(input(output), synType, isLoop)  # says the output and returns the prompt
            else:
                return input(output)
    # if the program does not want a response, aka: not a question
    else:

        # if the program has multiple statements to print out
        if isLoop:
            count = 0
            loopVector = len(output)
            while loopVector > count:  # while the number of statements is less than the number already stated, speak
                # say more
                if syntaxChk:
                    print(syntax.adv(output[count], synType), end=end)
                else:
                    print(output[count], end=end)
                count += 1

        # if the program does not want a loop
        else:
            if syntaxChk:
                print(syntax.adv(output, synType), end=end)
            else:
                print(output, end=end)

# incomplete function
def yamlWrite(value, element, File, isLoop=False, overwrite=False, update=False):
    if overwrite and not update:
        if isLoop:
            count = 0
            with open(File, "w") as file:
                while len(value) > count:
                    file.write(value[count])
                    count += 1
        else:
            with open(File, "w") as file:
                file.write(value)
    elif not overwrite and not update:
        if isLoop:
            count = 0
            with open(File, "a") as file:
                while len(value) > count:
                    file.write(value[count])
                    count += 1
        else:
            with open(File, "a") as file:
                file.write(value)

    if update:
        data = yamlRead(File, element, isLoop)

        if isLoop:
            count = 0
            while len(element) > count:
                data[element[count]].append(value[count])
                count += 1

        else:
            data[element] = value

        with open(File, "w") as file:
            yaml.dump(data, file)

def yamlRead(File, element, isLoop=False):
    with open(File, "r") as file:
        data = yaml.safe_load(file)

        if isLoop:
            count = 0
            out = []
            while len(data) > count:
                out.append(f"{element[count]}:{data[element[count]]}")

            return out
        else:
            return data
