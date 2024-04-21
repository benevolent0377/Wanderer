import fileinput
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
    OS = getOS()

    slash = getSlash()

    homePath = getHomePath()
    sysPath = getCWD()
    configPath = getConfigPath()

    configFile = configPath + "config.yaml"

    if os.path.isdir(configPath):

        if not os.path.isfile(configFile):
            open(configFile, "x")

    else:

        if os.mkdir(configPath) is not None:
            print("Failed to make configuration directory.")
            sys.exit()
        else:
            open(configFile, "x")

    web.fetchFTP(configFile, "config.yaml")

# check for internet condition
def isOnline():
    if not web.ping():
        print("No internet discovered. Please establish an internet connection before running this program.")
        return False
    else:
        return True

def getOS():
    return platform.platform().lower()

def getSlash():
    OS = getOS()
    if OS.find("linux") or OS.find("mac"):
        return "/"
    elif getOS().find("win"):
        return "\\"
    else:
        return "/"

def getHomePath():
    return os.path.expanduser("~") + getSlash()

def getCWD():
    return os.getcwd()

def getConfigPath():
    return getCWD() + getSlash() + "config" + getSlash()