from abc import ABC
class PrettyPrinter(ABC):
    @staticmethod
    def printSingular(jsonToPrint : dict, elements: dict):
        output = ""
        for key, printType in elements.items():
            if key  not in jsonToPrint.keys(): 
                output = key
            else: 
                output = jsonToPrint[key]

            if isinstance(printType, dict): PrettyPrinter.print(output, printType)
            elif (printType == "sameline"): print(f" {output}", end='')
            elif (printType == "comma"): print(f"{output}, ", end='')
            elif (printType == "header"): PrettyPrinter.printHeader(output)
            elif (printType == "text"): print(output)
            elif (printType == "siteInfo"): PrettyPrinter.printSiteInfo(output)
            elif (printType == "address"): PrettyPrinter.printAddress(jsonToPrint[key])
            else: print(f"{printType} is not a valid print type for {jsonToPrint[key]}")

    @staticmethod
    def print(jsonToPrint, elements):
        #If the object we are trying to print is in a list print all items
        if isinstance(jsonToPrint, list):
            for v in jsonToPrint:
                PrettyPrinter.print(v, elements)
            return
        elif isinstance(jsonToPrint, dict):
            PrettyPrinter.printSingular(jsonToPrint, elements)
            return


    @staticmethod
    def printHeader(message : str):
        print(f"---------------[{message}]---------------")

    @staticmethod
    def printAddress(message):
        PrettyPrinter.printSingular(message, {"unitNumber" : "comma", 
        "street" : "comma", 
        "street2" : "comma",    
        "suburb" : "text", 
        "state" : "comma",
        "postcode" : "text"})


    @staticmethod
    def printSiteInfo(message):
        typeKey = "facilityType"
        statusKey = "facilityStatus"
        timeKey = "waitingTime"
        bookingKey = "onSiteBooking"
        print(f"Facility Type: {message[typeKey]} -- Status {message[statusKey]} -- Wait time {message[timeKey]} -- Bookonsite {message[bookingKey]}")
        print()
