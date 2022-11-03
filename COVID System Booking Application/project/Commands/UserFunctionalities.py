from API_Handlers.User_Caller import UserCaller
from Command import Command
# Gets all users
class GetAllUsers(Command):
    def __init__(self, parent):
        super().__init__("Get all Users")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        output = UserCaller().get()
        print(output)
        self.parent.showCommands()


# Get User By ID
class GetUserByID(Command):
    def __init__(self, parent):
        super().__init__("Get User By ID")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        output = UserCaller().select()
        print(output)
        self.parent.showCommands()

#Create a new USer
class CreateNewUser(Command):
    def __init__(self,parent):
        super().__init__("Create new user")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        UserCaller().add("id")
        self.parent.showCommands()

class ViewNotifications(Command):
    def __init__(self, parent):
        super().__init__("View Notifications")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        id = self.getUserFromFile().id
        user = self.userCaller().getByID(id)
        if "notifications" not in user["additionalInfo"]:
            user["additionalInfo"].update({"notifications" : []})
        for notification in user["additionalInfo"]["notifications"]:
            print(notification)
        self.parent.showCommands()

class DeleteNotification(Command):
    def __init__(self, parent):
        super().__init__("Delete Notification")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        id = self.getUserFromFile().id
        user = self.userCaller().getByID(id)
        if "notifications" not in user["additionalInfo"]:
            user["additionalInfo"].update({"notifications" : []})
        for i, notification in enumerate(user["additionalInfo"]["notifications"]):
            print(f"{i + 1}. {notification}")
        if len(user["additionalInfo"]["notifications"]) == 0:
            print("There are no notifications to delete")
            return self.parent.showCommands()
        ans = int(input("Choose a booking to delete: ")) -1 
        user["additionalInfo"]["notifications"].pop(ans)
        self.userCaller().patch(user, user["id"])
        print("Removed")
        self.parent.showCommands()
