from abc import ABC
class UserInterface(ABC):
    @classmethod
    def __init__(cls, header, main=True):
        from Command import ExitCommand, GoToUI
        cls.header = header
        cls.commands = [ExitCommand()]
        if main:
            cls.commands.append(GoToUI(HomeUI, "Main Menu", cls))

    @classmethod
    def filterCommands(cls):    
        from GlobalConstants import AUTHORISATIONS, GetUserFromFile
        USER = GetUserFromFile()
        userAuth = [AUTHORISATIONS.DEFAULT]
        if USER is not None:
            USER.authorisations.append(AUTHORISATIONS.DEFAULT)
            userAuth = USER.authorisations

        commandsToRemove = []
        for command in cls.commands:
            commandValid = False
            for commandAuth in command.authorisations:
                if commandAuth in userAuth:
                    commandValid = True

            if (not commandValid):
                commandsToRemove.append(command)

        for com in commandsToRemove:
            cls.commands.remove(com)

    @classmethod
    def showCommands(cls):
        cls.filterCommands()
        print(f"\n{cls.header}")
        for i, command in enumerate(cls.commands):
            print(f"{i + 1}: {command.message}")
        userInput = int(input()) - 1
        cls.commands[userInput].executeCommand()


# --------Here is where we will define some subclasses for different UI menus---------------------
# Logging in
class Login(UserInterface):
    def __init__(self):
        from Commands.TestingSiteFunctionalities import ViewTestingSites
        from Command import LoginCommand
        from Commands.UserFunctionalities import CreateNewUser
        super().__init__("Login Menu", False)
        self.commands.append(LoginCommand())
        self.commands.append(ViewTestingSites(self))


# Home menu
class HomeUI(UserInterface):
    def __init__(self):
        from Command import GoToUI
        super().__init__("Please choose a command from below!", False)
        self.commands.append(GoToUI(NotificationUI, "Notifications"))
        self.commands.append(GoToUI(BookingUI, "Go to bookings"))
        self.commands.append(GoToUI(TestingSiteUI, "Go to Testing Site Manager"))
        self.commands.append(GoToUI(CovidTestUI, "Go to Covid Test Manager"))
        self.commands.append(GoToUI(UserUI, "Go to User Manager"))

class NotificationUI(UserInterface):
    def __init__(self):
        from Commands.UserFunctionalities import ViewNotifications, DeleteNotification
        super().__init__("Testing Site Manager")
        self.commands.append(ViewNotifications(NotificationUI))
        self.commands.append(DeleteNotification(NotificationUI))


class TestingSiteUI(UserInterface):
    def __init__(self):
        from Commands.TestingSiteFunctionalities import ViewTestingSites, DeleteTestingSite, AddTestingSite, \
            EditTestingSite, GetSiteByID, GetSiteBySuburbNameOrType
        super().__init__("Testing Site Manager")
        self.commands.append(ViewTestingSites(TestingSiteUI))
        self.commands.append(DeleteTestingSite(TestingSiteUI))
        self.commands.append(AddTestingSite(TestingSiteUI))
        self.commands.append(EditTestingSite(TestingSiteUI))
        self.commands.append(GetSiteByID(TestingSiteUI))
        self.commands.append(GetSiteBySuburbNameOrType(TestingSiteUI))



class BookingUI(UserInterface):
    def __init__(self):
        from Commands.BookingFunctionalities import GetBookings, CreateBooking, OnSiteBooking, HomeBooking, ApproveHomeBooking, DeleteBooking
        from Command import GoToUI
        super().__init__("Booking Menu")
        self.commands.append(GetBookings(BookingUI))
        self.commands.append(CreateBooking(BookingUI))
        self.commands.append(GoToUI(ModifyBooking, "Current Bookings"))
        self.commands.append(OnSiteBooking(BookingUI))
        self.commands.append(HomeBooking(BookingUI))
        self.commands.append(ApproveHomeBooking(BookingUI))

class CovidTestUI(UserInterface):
    def __init__(self):
        from Commands.CovidTestFunctionalities import GetCovidTest, CreateTest
        super(CovidTestUI, self).__init__("Covid Test Menu")
        self.commands.append(GetCovidTest(CovidTestUI))
        self.commands.append(CreateTest(CovidTestUI))


class UserUI(UserInterface):
    def __init__(self):
        from Commands.UserFunctionalities import GetAllUsers, GetUserByID, CreateNewUser
        super(UserUI, self).__init__("User Menu")
        self.commands.append(GetAllUsers(UserUI))
        self.commands.append(GetUserByID(UserUI))
        self.commands.append(CreateNewUser(UserUI))

class ModifyBooking(UserInterface):
    def __init__(self) -> None:
        from API_Handlers.Booking_Caller import BookingCaller
        from Commands.BookingFunctionalities import CancelBooking, EditBooking, DeleteBooking, RevertBooking
        from GlobalConstants import GetUserFromFile, AUTHORISATIONS

        print("Which booking would you like to modify?")
        if AUTHORISATIONS.RECEPTIONIST in GetUserFromFile().authorisations:
            output = BookingCaller().select()
        else:
            output = BookingCaller().select(GetUserFromFile().id, True)

        if output is not None:
            super(ModifyBooking, self).__init__(f"Modify Booking {output['id']}")
            self.commands.append(CancelBooking(BookingUI, output))
            self.commands.append(EditBooking(BookingUI, output))
            self.commands.append(DeleteBooking(BookingUI, output))
            self.commands.append(RevertBooking(BookingUI, output))
        else:
            super(ModifyBooking, self).__init__(f"No Bookings Selected")

