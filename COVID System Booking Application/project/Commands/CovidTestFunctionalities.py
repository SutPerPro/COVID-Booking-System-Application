from API_Handlers.Covid_Test_Caller import CovidTestCaller
from Command import Command
# ets all covid tests NW
class GetCovidTest(Command):
    def __init__(self, parent):
        super().__init__("Get Covid Tests")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        output = self.covidTestCaller().get()
        # PrettyPrinter.print(output, {"id" : })
        print(output)
        self.parent.showCommands()

class CreateTest(Command):
    def __init__(self, parent):
        super().__init__("Create Test")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        format = {
            "type": "PCR",
            "patientId": self.userCaller().select()["id"],
            "administererId": self.userCaller().select()["id"],
            "bookingId": "string",
            "result": "POSITIVE",
            "status": "string",
            "notes": "string",
            }

        for key in format.keys():
            if key == "patientId": continue
            format[key] = input(f"{key}")
        resp = self.covidTestCaller().post(format)
        if resp.status_code == 201:
            print("Test Recorded")
            return