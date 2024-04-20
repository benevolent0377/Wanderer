# a file of local inout functions making the process easy and keeping the main file decluttered

def say(output, isQuestion):

    # checking if the program wants a response
    if isQuestion:

        return input(output)
    # if the program does not want a response
    else:
        print(output)

