import fileinput
import platform
import os
import sys
import datetime
from . import web
from . import extra
from . import IO

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
    tmpPath = getTmpPath()

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

    if not os.path.isfile(f"{configPath}{slash}local.yaml"):
        File = f"{configPath}{slash}local.yaml"
        if IO.mkFile(File):
            elements = ["OS", "CWD", "Home-Directory", "Program-SerialNo"]
            values = [OS, sysPath, homePath, extra.keyGen(24)]
            IO.yamlWrite(values, elements, File, True)
        else:
            IO.say("Failed to create local configuration file.")
            sys.exit()


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

def getTmpPath():
    return f"{getCWD()}{getSlash()}tmp{getSlash()}"

def getDT(date=True, time=True):

    if date and time:
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif time and not date:
        return datetime.datetime.now().strftime('%H:%M:%S')
    elif date and not time:
        return datetime.datetime.now().strftime('%Y-%m-%d')

# deleting all files in the tmp directory
def clearCache():
    tmpPath = getTmpPath()
    tmpFiles = os.listdir(tmpPath)
    for file in tmpFiles:
        os.remove(f"{tmpPath}{file}")