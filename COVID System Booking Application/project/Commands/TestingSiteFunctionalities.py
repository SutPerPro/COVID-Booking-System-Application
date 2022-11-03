
from Command import Command
from API_Handlers.Sites_Caller import SitesCaller
from Printing import PrettyPrinter
# Show testing sites FW
class ViewTestingSites(Command):
    def __init__(self, parent):
        super().__init__("Show Testing Sites")
        self.parent = parent

    def executeCommand(self):
        output = self.siteCaller().get()
        PrettyPrinter.print(output, {"name": "header", "description": "text", "address": "address"})
        self.parent.showCommands()

# Add A Site FW
class AddTestingSite(Command):
    def __init__(self, parent):
        super().__init__("Add New Testing Sites")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        self.siteCaller().add()
        self.parent.showCommands()

# Get Testing Site By ID
class GetSiteByID(Command):
    def __init__(self, parent):
        super().__init__("Get Testing Site by ID")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]


    def executeCommand(self):
        output = self.siteCaller().select()
        print(output)
        self.parent.showCommands()

# Edit A Site PW
class EditTestingSite(Command):
    def __init__(self, parent):
        super().__init__("Edit Testing Sites")
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]
        self.parent = parent

    def executeCommand(self):
        testingSiteId = self.siteCaller().select()["id"]
        attributeToChange = input("Enter Attribute to Change: ")
        self.siteCaller().update(attributeToChange, testingSiteId)
        self.parent.showCommands()

# Delete A Site FW
class DeleteTestingSite(Command):
    def __init__(self, parent):
        super().__init__("Delete Testing Sites")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]


    def executeCommand(self):
        id = self.siteCaller().select()["id"]
        self.siteCaller().delete(id)
        self.parent.showCommands()

#Search Testing Site by Name or Type
class GetSiteBySuburbNameOrType(Command):
    def __init__(self, parent):
        super().__init__("Search Site")
        self.parent = parent
    def executeCommand(self):
        from Filters.Filter_Search import FilterSearchByAttribute
        layer = []
        if (eval(input("Search by address (True/False)"))):
            layer = ["address"]
            category = "suburb"
        elif (eval(input("Search by clinic (True/False)"))):
            layer = ["additionalInfo"]
            category = "facilityType"
        else: 
            self.parent.showCommands()
            return
        searchInput = input("Search: ")
        output = self.siteCaller().get()
        filtered = FilterSearchByAttribute(category,searchInput,layer).filter(output)
        PrettyPrinter.print(filtered, {"name" : "text", "address" : "address", "additionalInfo" : "siteInfo"})

        self.parent.showCommands()
