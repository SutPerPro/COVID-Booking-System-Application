import datetime
from Command import Command
from Printing import PrettyPrinter

# Get All Bookings FW
class GetBookings(Command):
    def __init__(self, parent):
        super().__init__("Get All Bookings")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        output = self.bookingCaller().get()
        PrettyPrinter.print(output, {"customer":
                                         {"givenName": "sameline",
                                          "familyName": "sameline",
                                          "--": "sameline",
                                          "phoneNumber": "sameline",
                                          "-- at": "sameline"},
                                     "testingSite": {"name": "sameline",
                                                     "--": "sameline"},
                                     "status": "sameline",
                                     "startTime": "text"})
        print()
        self.parent.showCommands()

# Notify Admin
class NotifyAdmins(Command):
    def __init__(self, message):
        super().__init__("Notify Admin")
        self.message = f"{message} - {datetime.datetime.now()}"

    def executeCommand(self):
        users = self.userCaller().get()
        for user in users:
            if user["isReceptionist"]:
                if "notifications" not in user["additionalInfo"]:
                    user["additionalInfo"].update({"notifications" : []})
                user["additionalInfo"]["notifications"].append(self.message)
                self.userCaller().patch(user,user["id"])

# Creates New Bookings PW
class CreateBooking(Command):
    def __init__(self, parent):
        super().__init__("Create Booking")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        print("Users")
        customerId = self.userCaller().select()["id"]
        print("TestingSites")
        testingSiteId = self.siteCaller().select()["id"]
        startTime = input("Enter Time: ")
        notes = input("Enter notes: ")
        booking = {"customerId": customerId, "testingSiteId": testingSiteId, "startTime": startTime, "notes": notes}
        self.bookingCaller().post(booking)
        self.parent.showCommands()


#Cancel Booking
class CancelBooking(Command):
    def __init__(self, parent, booking):
        super().__init__("Cancel Booking")
        self.parent = parent
        self.booking = booking

    def executeCommand(self):
        self.bookingCaller().patch({"status" : "CANCELLED"}, self.booking["id"])
        notification = f"The booking for {self.booking['customer']['givenName']} {self.booking['customer']['familyName']} has been cancelled - ID {self.booking['id']}"
        NotifyAdmins(notification).executeCommand()
        print("Cancelled")
        self.parent.showCommands()


class RevertBooking(Command):
    def __init__(self, parent, booking):
        super().__init__("Revert Booking")
        self.booking = booking
        self.parent = parent

    def executeCommand(self):
        print("Please select change to rollback to")
        for i, change in enumerate(self.booking["additionalInfo"]["changes"]):
            site = self.siteCaller().getByID(change[1][1])["name"]
            date = change[0][1]
            print(f"{i+1}. At {site} on date {date}, edited on {change[2]}")
        print(f"{i + 2}. None")
        changeIndex = int(input()) - 1
        self.bookingCaller().reverseChange(self.booking["id"],self.booking["additionalInfo"]["changes"][changeIndex])
        notification = f"The booking for {self.booking['customer']['givenName']} {self.booking['customer']['familyName']} has been reverted - ID {self.booking['id']}"
        print("Rolled Back!")
        NotifyAdmins(notification).executeCommand()
        self.parent.showCommands()

class DeleteBooking(Command):
    def __init__(self, parent, booking):
        super().__init__("Delete Booking")
        self.parent = parent
        self.booking = booking
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST]

    def executeCommand(self):
        caller = self.bookingCaller()
        caller.delete(self.booking["id"])
        if caller.status == 204:
            print("Deleted")
            notification = f"A booking has been deleted. Booking ID: {self.booking['id']}"
            NotifyAdmins(notification).executeCommand()
        self.parent.showCommands()

class EditBooking(Command):
        def __init__(self, parent, booking):
            super().__init__("Edit Booking")
            self.parent = parent
            self.booking = booking

        def executeCommand(self):
            testingSiteId = self.siteCaller().select()["id"]
            time = input("What time would you like to change it to? ")
            bookingJson = {
                    "customerId": self.booking["customer"]["id"],
                    "testingSiteId": testingSiteId,
                    "startTime": time,
                    "status": self.booking["status"],
                    "notes": self.booking["notes"],
                    "additionalInfo": self.booking["additionalInfo"]
            }
            caller = self.bookingCaller()
            caller.patch(bookingJson, self.booking["id"])
            if caller.status == 200:
                caller.storeChanges(self.booking["id"], [["startTime", self.booking["startTime"]], ["testingSiteId", self.booking["testingSite"]["id"]]])
                notification = f"The booking for {self.booking['customer']['givenName']} {self.booking['customer']['familyName']} has been changed - ID {self.booking['id']}"
                NotifyAdmins(notification).executeCommand()
            self.parent.showCommands()


# On Site Booking
class OnSiteBooking(Command):
    def __init__(self, parent):
        super().__init__("On Site Booking")
        self.parent = parent

    def executeCommand(self):
        print("Users")
        customerId = self.userCaller().select()["id"]
        print("TestingSites")
        testingSiteId = self.siteCaller().select()["id"]
        if not(self.siteCaller().getByID(testingSiteId)["additionalInfo"]["onSiteBooking"]):
            print("Site does not support onSiteBooking")
            self.parent.showCommands()
            return
        startTime = input("Enter Time: ")
        notes = input("Enter notes: ")
        booking = {"customerId": customerId, "testingSiteId": testingSiteId, "startTime": startTime, "notes": notes}
        self.bookingCaller().post(booking)
        self.parent.showCommands()

class HomeBooking(Command):
    def __init__(self, parent):
        super().__init__("Home Booking")
        self.parent = parent

    def executeCommand(self):
        from API_Handlers.Sites_Caller import SitesCaller
        if self.AUTHORISATIONS.CUSTOMER in self.getUserFromFile().authorisations and self.AUTHORISATIONS.RECEPTIONIST not in self.getUserFromFile().self.authorisations:
            customerId = self.getUserFromFile().id
        else:
            print("Users")
            customerId = self.userCaller().select()["id"]
        print("Sites")
        testingSiteId = SitesCaller().select()["id"]
        startTime = input("Enter Time: ")
        notes = input("Enter notes: ")
        booking = {"customerId": customerId, 
        "testingSiteId": testingSiteId, 
        "startTime": startTime, 
        "notes": notes,
        "additionalInfo" : {"homeTest" : True, "approved" : False, "url" : "string", "QR" : customerId[3:7]}}
        self.bookingCaller().post(booking)
        self.parent.showCommands()


class ApproveHomeBooking(Command):
    def __init__(self, parent):
        super().__init__("Approve Test")
        self.parent = parent
        self.authorisations = [self.AUTHORISATIONS.RECEPTIONIST, self.AUTHORISATIONS.HEALTHCAREWORKER]

    def executeCommand(self):
        bookId = self.bookingCaller().select["id"]
        approved = input("Approve? ('True'/'False') : ")
        if eval(approved):
            url = input("Online testing url: ")
        else:
            approved = input("Delete booking? ('True'/'False') : ")
            if eval(approved):
                self.bookingCaller().delete(bookId)
            return
        self.bookingCaller().patch({"additionalInfo" : {"approved" : eval(approved), "url" : url}},bookId)
        self.parent.showCommands()


