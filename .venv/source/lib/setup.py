import platform


# a file to initialize the files and services needed to run the program

def run():
    fileSetup()


def fileSetup():
    OS = platform.platform().lower()

    if OS.find("linux") or OS.find("mac"):
        slash = "/"
    elif OS.find("win"):
        slash = "\\"
    else:
        slash = "/"
