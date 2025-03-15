import datetime
import os
import platform

from . import IO, extra, log, web, syntax


# a file to initialize the files and services needed to run the program
def init(directoriesReq, filesReq, onlineReq=False):
    global logID
    global sysDT
    logID = extra.keyGen(6)
    sysDT = getDT()

    fileSetup(directoriesReq, filesReq)

    if onlineReq:
        if not isOnline():
            quitKill()
        #IO.say("--- NOTICE Internet Capabilities Currently Disabled... NOTICE ---\n")

def fileSetup(directoriesReq, filesReq=""):
    slash = getSlash()

    for directory in directoriesReq:
        path = getCWD() + slash + directory + slash
        if not os.path.isdir(path):
            if not IO.mkDir(path):
                IO.say("Failed to create vital directory.")
                log.log("dir creation failed.", "err")
                quitKill()

    if filesReq != "":
        for file in filesReq:
            path = getCWD() + slash + file
            if not os.path.isfile(path):
                if not IO.mkFile(path):
                    IO.say("Failed to create vital files.")
                    log.log("dir creation failed.", "err")
                    quitKill()


# check for internet condition
def isOnline():
    if not web.ping():
        print("No internet discovered. Please establish an internet connection before running this program.")
        return False
    else:
        return True


def getOS():
    return str(platform.system().lower())


def getSlash():
    OS = getOS()
    if OS.find("linux") != -1 or OS.find("mac") != -1:
        return "/"
    elif OS.find("win") != -1:
        return "\\"


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
    logName = f"{sysDT.replace(':', '').replace(' ', '_')}_{logID}.log.txt"
    logFile = f"{getLogPath()}{logName}"

    return [logID, logName, logFile, sysDT]

def getDataPath():
    return f"{getCWD()}{getSlash()}data{getSlash()}"

def getDownloadPath():
    return f"{getCWD()}{getSlash()}downloads{getSlash()}"

def getAssetsPath():
    return f"{getCWD()}{getSlash()}assets{getSlash()}"

# the quit function
def quitKill(preserve=False):
    if not preserve:
        clearCache()
    log.log("", "quit")
    exit()

def dumpHead():
    IO.say(['Created by: Benevolent0377', f'Version: {IO.yamlRead(f"{getConfigPath()}local.yaml", "Version")}', f'SessionID: {logID}', '===========================================\n\n'], isLoop=True)
