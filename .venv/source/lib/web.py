import socket
import ftplib
from . import IO
from . import setup
# a file for all the HTTP and HTTPS functions
hostName = "calithos.in"
usr = "wanderer@calithos.in"
pwd = "USYuQPD41"

def ping(host="8.8.8.8", port=53, timeout=3):
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
        print(ex)
        return False

def fetchFTP(localFile, remoteFile, timeout=2000):
    with ftplib.FTP(hostName, timeout=timeout) as ftp:
        ftp.login(user=usr, passwd=pwd)
        ftp.encoding = "utf-8"
        with open(localFile, "wb") as file:
            ftp.retrbinary(f"RETR {remoteFile}", file.write)


def postFTP(localFile, remoteFile, timeout=2000, isTmp=False):
    with ftplib.FTP(hostName, timeout=timeout) as ftp:
        ftp.login(user=usr, passwd=pwd)
        ftp.encoding = "utf-8"
        if isTmp:
            with open(localFile, "xw") as file:
                file.write(IO.yamlRead(f"{setup.getConfigPath()}{setup.getSlash()}local.yaml", "Program-SerialNo"))

                ftp.storbinary(f"STOR {remoteFile}", file)

        else:
            with open(localFile, "xw") as file:
                file.write(IO.yamlRead(f"{setup.getConfigPath()}{setup.getSlash()}local.yaml", "Program-SerialNo"))

                ftp.storbinary(f"STOR {remoteFile}", file)