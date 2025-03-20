#this file will handle all error codes for the core files, as well as allowing for the creation of custom error codes

errors = {"1": "Undefined Error"]

def addErrors(customErrors):
    global errors
    for errorCode, errorDesc in customErrors.items():
        errors.update({errorCode: errorDesc})

def getAll():
    global errors
    return errors

def parse(command, successStmt, failureStmt, errorCode = "1"):
    try:
        exec(command)
        print(successtStmt)
    except:
        print(f"{errorCode} {errors[errorCode]}: {failureStmt})
