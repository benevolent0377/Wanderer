import platform
import os
import sys
from . import web

# a file to initialize the files and services needed to run the program

def run():
    fileSetup()

    if not isOnline():
        sys.exit()



def fileSetup():
    OS = platform.platform().lower()

    if OS.find("linux") or OS.find("mac"):
        slash = "/"
    elif OS.find("win"):
        slash = "\\"
    else:
        slash = "/"

    homePath = os.path.expanduser("~") + slash
    sysPath = os.getcwd()
    configPath = sysPath + slash + "config" + slash

    configFile = configPath + "config.yaml"

    if os.path.isdir(configPath):

        if not os.path.isfile(configFile):
            print("hello")

    else:
        if os.mkdir(configPath) is not None:
            print("Failed to make configuration directory.")
            sys.exit()
        else:
            print("hello")

# check for internet condition
def isOnline():
    if not web.ping():
        print("No internet discovered. Please establish an internet connection before running this program.")
        return False
    else:
        return True