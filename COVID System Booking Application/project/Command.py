from API_Handlers.Booking_Caller import BookingCaller
from API_Handlers.User_Caller import UserCaller
from API_Handlers.Covid_Test_Caller import CovidTestCaller
from API_Handlers.Sites_Caller import SitesCaller
from GlobalConstants import AUTHORISATIONS, GetUserFromFile
from typing import Type
from abc import ABC
from Authentication import Authentication



class Command(ABC):
    def __init__(self, message):
        self.message = message
        self.authorisations = [AUTHORISATIONS.DEFAULT]
        self.AUTHORISATIONS = AUTHORISATIONS
        self.getUserFromFile = GetUserFromFile
        self.bookingCaller = BookingCaller
        self.userCaller = UserCaller
        self.siteCaller = SitesCaller
        self.covidTestCaller = CovidTestCaller
        if message is None: self.message = ""

    def executeCommand(cls):
        pass


###Different Command Strategies
# Exit
class ExitCommand(Command):
    def __init__(self):
        super().__init__("Exit")

    def executeCommand(self):
        exit()


# Login
class LoginCommand(Command):
    def __init__(self):
        super().__init__("Login")

    def executeCommand(self):
        from UI import HomeUI, Login
        import json
        from GlobalConstants import GetUserFromFile
        userJson = Authentication.verifyLogin()
        with open('USER.txt', 'w') as f:
            f.write(json.dumps(userJson))
        USER = GetUserFromFile()
        if USER is None:
            print("Login failed")
            Login().showCommands()
        print(f"Login successful {USER.givenName}")
        GoToUI(HomeUI).executeCommand()


# Show UI
class GoToUI(Command):
    from UI import UserInterface
    def __init__(self, ui: Type[UserInterface], message=None, parent=None):
        super().__init__(message)
        self.parent = parent
        self.ui = ui

    def executeCommand(self):
        ui = self.ui()
        if self.parent is not None:
            ui.commands.append(GoToUI(self.parent, "Back"))
        ui.showCommands()

