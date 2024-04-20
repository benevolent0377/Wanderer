# a file of local inout functions making the process easy and keeping the main file decluttered
from typing import List


def say(output, isQuestion = False, isLoop = False, end="\n", syntaxCheck = False):

    # checking if the program wants a response
    if isQuestion:

        # seeing if the program wants to ask multiple queries
        if isLoop:
            loopVector = len(output)
            count = 0
            usrSay = [""]
            while loopVector > count:
                usrSay[loopVector] = input(output[loopVector])
                count += 1
            return usrSay

        else:
            return input(output)
    # if the program does not want a response
    else:

        # if the program has multiple statements to print out
        if isLoop:
            count = 0
            loopVector = len(output)
            while loopVector > count:
                print(output[count], end=end)
                count += 1

        # if the program does not want a loop
        else:
            print(output, end=end)

