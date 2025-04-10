import ftplib, hashlib
import requests
from source.core import IO, log, system

# a file for all the HTTP and HTTPS functions
hostName = "calithos.in"
usr = "wanderer@calithos.in"
pwd = "USYuQPD41"


def fetchFTP(localFile, remoteFile, timeout=45):
    IO.say("Establishing FTP connection...\n")
    with ftplib.FTP(hostName, timeout=timeout) as ftp:
        ftp.login(user=usr, passwd=pwd)
        log.log(hostName, "ftpconnect", usr)
        ftp.encoding = "utf-8"
        with open(localFile, "wb") as file:
            ftp.retrbinary(f"RETR {remoteFile}", file.write)
            log.log(remoteFile, "ftpD", hostName)
            IO.say("Done.")


def postFTP(localFile, remoteFile, timeout=45, isTmp=False, isYaml=False, keyword=""):
    with ftplib.FTP(hostName, timeout=timeout) as ftp:
        ftp.login(user=usr, passwd=pwd)
        log.log(hostName, "ftpconnect", usr)
        ftp.encoding = "utf-8"
        if isTmp:

            with open(localFile, "xw") as file:
                if isYaml:
                    data = IO.yamlRead(localFile, keyword)
                    file.write(data)
                else:
                    file = IO.fileRead(localFile)

                ftp.storlines(f"STOR {remoteFile}", file)
                log.log(remoteFile, "ftpD", hostName)

        else:

            with open(localFile, "xw") as file:
                if isYaml:
                    data = IO.yamlRead(localFile, keyword)
                    file.write(data)
                else:
                    file = IO.fileRead(localFile)

                ftp.storlines(f"STOR {remoteFile}", file)
                log.log(remoteFile, "ftpD", hostName)

def HTTPget(host, destination, timeout=45):
    if web.ping(host, 443, timeout):
        IO.say("Host reached")
    else:
        IO.say("Host Unavaliable")
    print()

def getParentCFG():

    configURL = "https://api.github.com/repositories/789248032/contents/config"
    slash = system.getSlash()
    configPath = system.getCWD() + slash + "config" + slash + "parent.yaml"
    configDataRaw = requests.get(configURL).json()

    completion = False

    configData = configDataRaw[0]

    downloadURL = configData["download_url"]
    remoteContent = requests.get(downloadURL).text

    localContent = IO.fileRead(configPath)
    localContentString = ""

    for line in localContent:
        localContentString += line

    localmd5 = hashlib.md5(localContentString.encode()).hexdigest()
    remotemd5 = hashlib.md5(remoteContent.encode()).hexdigest()

    if remotemd5 != localmd5:
        IO.rmFile(configPath)
        IO.mkFile(configPath)
        IO.fileWrite(remoteContent, configPath, overwrite = True)
    
    completion = True

    return completion
