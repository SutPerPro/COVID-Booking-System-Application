##DO NOT CHANGE CONSTANT VALUES
from fileinput import filename
import json
from user import User

def GetUserFromFile():
    fileName = "USER.txt"
    if emptyFile(fileName):
        return None
    else: 
        with open(fileName) as f:
            firstLine = f.readline()
            if firstLine == "null":
                return None
            return  User(json.loads(firstLine))
        

def emptyFile(file_name):
    with open(file_name, 'r') as f:
        # read first character
        char = f.read(1)
        # if not fetched then file is empty
        if not char:
           return True
    return False


#The exception is user which should only ever be changed at the initial user interface
USER = GetUserFromFile()

class AUTHORISATIONS:
    DEFAULT = 0
    CUSTOMER = 1
    RECEPTIONIST = 2
    HEALTHCAREWORKER = 3 

