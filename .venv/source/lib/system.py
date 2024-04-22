import fileinput
import platform
import os
import sys
import datetime
from . import log
from . import web
from . import extra
from . import IO
from . import main


# a file to initialize the files and services needed to run the program
def init():
    global logID
    global sysDT
    logID = extra.keyGen(6)
    sysDT = getDT()

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
    logPath = getLogPath()

    configFileP = f"{configPath}parent.yaml"
    configFileL = f"{configPath}local.yaml"

    if os.path.isdir(configPath):

        if not os.path.isfile(configFileP):
            open(configFileP, "x")

    else:

        if not IO.mkDir(configPath):
            print("Failed to make configuration directory.")
            main.quitKill()
        else:
            log.log(configPath, "mkdir")
            open(configFileP, "x")

    web.fetchFTP(configFileP, "parent.yaml")

    if not os.path.isfile(configFileL):
        if IO.mkFile(configFileL):
            elements = ["OS", "CWD", "Home-Directory", "Program-SerialNo", "SendLogs"]
            values = [OS, sysPath, homePath, extra.keyGen(24), "False"]
            IO.yamlWrite(values, elements, configFileL, True)
        else:
            IO.say("Failed to create local configuration file.")
            main.quitKill()

    log.init(configFileL, logPath)

    if not os.path.isdir(tmpPath):
        if not IO.mkDir(tmpPath):
            IO.say("Failed to create temporary directory.")
            main.quitKill()

    sendLogs(configFileL)

def sendLogs(configFileL):

    if IO.yamlRead(configFileL, "SendLogs").__eq__('False'):
        response = IO.say("Would you like to opt into uploading log data? It IS anonymous. DEFAULT is no. (yes/no)", True, syntaxChk=True, synType="internal")
        if response.__eq__("yes") or response.eq("y"):
            IO.yamlWrite("True", "SendLogs", configFileL)
    IO.say("Thank you for using Wanderer.py!")

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


def getLogPath():
    return f"{getCWD()}{getSlash()}log{getSlash()}"


# deleting all files in the tmp directory
def clearCache():
    tmpPath = getTmpPath()
    tmpFiles = os.listdir(tmpPath)
    for file in tmpFiles:
        os.remove(f"{tmpPath}{file}")
        log.log(f"{tmpPath}{file}", "del")


def getLogInfo():
    logName = f"wanderer_{sysDT}_{logID}.log.txt"
    logFile = f"{getLogPath()}{logName}"

    return [logID, logName, logFile, sysDT]
