import socket
import ftplib
import requests
from . import IO, log

# a file for all the HTTP and HTTPS functions
hostName = "calithos.in"
usr = "wanderer@calithos.in"
pwd = "USYuQPD41"

def ping(host="8.8.8.8", port=53, timeout=10):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        log.log(ex, "err")
        return False

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

def HTTPget(host, returnType='bytes', timeout=45):

    data = requests.get(host)

    match returnType:
        case 'bytes':
            return data.content
        case 'text':
            return data.text
        case 'head':
            return data.headers
        case 'json':
            return data.json
        case 'code':
            return data.status_code
        case 'boolean':
            return data.ok

    print()
