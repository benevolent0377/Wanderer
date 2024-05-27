import os
from source.core import IO, system, extra, log
from . import internet

def mkConfig():
    OS = system.getOS()
    slash = system.getSlash()

    configFileP = f"{system.getConfigPath()}parent.yaml"
    configFileL = f"{system.getConfigPath()}local.yaml"
    sysPath = system.getCWD()
    homePath = system.getHomePath()
    logPath = system.getLogPath()

    internet.fetchFTP(configFileP, "parent.yaml")

    if not os.path.isfile(configFileL):
        if IO.mkFile(configFileL):
            elements = ["OS", "CWD", "Home-Directory", "Program-SerialNo", "SendLogs", "Version"]
            values = [OS, sysPath, homePath, extra.keyGen(24), " ", "1.0.0 Alpha"]
            IO.yamlWrite(values, elements, configFileL, True)
        else:
            IO.say("Failed to create local configuration file.")
            log.log("local.config creation failed.", "err")
            system.quitKill()

    log.init(configFileL, logPath)

    sendLogs(configFileL)

def sendLogs(configFileL):

    if IO.yamlRead(configFileL, "SendLogs").__eq__(' '):
        response = IO.say("Would you like to opt into uploading log data? It IS anonymous. DEFAULT is no. (yes/no)", True, syntaxChk=True, synType="internal")
        if response.__eq__("yes") or response.__eq__("y"):
            IO.yamlWrite("True", "SendLogs", configFileL)
        else:
            IO.yamlWrite("False", "SendLogs", configFileL)
        IO.say("Thank you for using source.py!")

