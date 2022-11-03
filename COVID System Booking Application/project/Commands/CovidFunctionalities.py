from Command import Command
from API_Handlers.Covid_Test_Caller import CovidTestCaller

class CreateTest(Command):
    def __init__(self, parent):
        super().__init__("Create Test")
        self.parent = parent

    def executeCommand(self):
        format = {
            "type": "PCR",
            "patientId": "string",
            "administererId": "string",
            "bookingId": "string",
            "result": "POSITIVE",
            "status": "string",
            "notes": "string",
            }

        for key in format.keys():
            format[key] = input(f"{key}")
        resp = self.covidTestCaller().post(["id"])
        if resp.status_code == 201:
            print("Test Recorded")
            return
        print(f"ERROR: {resp.status_code}")
