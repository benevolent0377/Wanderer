# a file of local inout functions making the process easy and keeping the main file decluttered
from typing import List


# simply prints the string output or creates a query in the terminal, also returns the inputted values
def say(output, isQuestion=False, isLoop=False, end="\n", syntaxCheck=False):
    # checking if the program wants a response, aka: question = yes
    if isQuestion:

        # seeing if the program wants to ask multiple queries
        if isLoop:
            loopVector = len(output)
            count = 0
            usrSay = []  # this is the returned list
            while loopVector > count:   # while the # of questions is greater than the responses, ask a question
                usrSay.append(input(output[count]))
                count += 1
            return usrSay

        else:
            return input(output)  # says the output and returns the prompt

    # if the program does not want a response, aka: not a question
    else:

        # if the program has multiple statements to print out
        if isLoop:
            count = 0
            loopVector = len(output)
            while loopVector > count:   # while the number of statements is less than the number already stated, speak
                # say more
                print(output[count], end=end)
                count += 1

        # if the program does not want a loop
        else:
            print(output, end=end)
