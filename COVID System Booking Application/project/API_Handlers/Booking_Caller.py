from API_Handlers.API_Caller import APICaller


class BookingCaller(APICaller):
    def __init__(cls) -> None:
        booking = {
            "id": "string",
            "customer": {
                "id": "string",
                "givenName": "string",
                "familyName": "string",
                "userName": "string",
                "phoneNumber": "string",
                "isCustomer": True,
                "isReceptionist": True,
                "isHealthcareWorker": True,
                "additionalInfo": {}
            },
            "testingSite": {
                "id": "string",
                "name": "string",
                "description": "string",
                "websiteUrl": "string",
                "phoneNumber": "string",
                "address": {
                    "latitude": 0,
                    "longitude": 0,
                    "unitNumber": "string",
                    "street": "string",
                    "street2": "string",
                    "suburb": "string",
                    "state": "string",
                    "postcode": "string",
                    "additionalInfo": {}
                },
                "createdAt": "2022-04-28T14:22:38.195Z",
                "updatedAt": "2022-04-28T14:22:38.195Z",
                "additionalInfo": {}
            },
            "createdAt": "2022-04-28T14:22:38.195Z",
            "updatedAt": "2022-04-28T14:22:38.195Z",
            "startTime": "2022-04-28T14:22:38.195Z",
            "smsPin": "string",
            "status": "string",
            "covidTests": [
                {
                    "id": "string",
                    "type": "string",
                    "patient": {
                        "id": "string",
                        "givenName": "string",
                        "familyName": "string",
                        "userName": "string",
                        "phoneNumber": "string",
                        "isCustomer": True,
                        "isReceptionist": True,
                        "isHealthcareWorker": True,
                        "additionalInfo": {}
                    },
                    "administerer": {
                        "id": "string",
                        "givenName": "string",
                        "familyName": "string",
                        "userName": "string",
                        "phoneNumber": "string",
                        "isCustomer": True,
                        "isReceptionist": True,
                        "isHealthcareWorker": True,
                        "additionalInfo": {}
                    },
                    "result": "string",
                    "status": "string",
                    "notes": "string",
                    "datePerformed": "2022-04-28T14:22:38.195Z",
                    "dateOfResults": "2022-04-28T14:22:38.195Z",
                    "createdAt": "2022-04-28T14:22:38.195Z",
                    "updatedAt": "2022-04-28T14:22:38.195Z",
                    "additionalInfo": {}
                }
            ],
            "notes": "string",
            "additionalInfo": {
                "changes" : [],
            }
        }
        return super().__init__("/booking", booking)


    def select(self, customer = None, openBookingsOnly = False):
        values : list = self.get()
        removed = []
        if customer is not None:
            for value in values:
                if value["customer"]["id"] != customer:
                    removed.append(value)
        if openBookingsOnly:
            for value in values:
                if value["status"] == "COMPLETED" or value["status"] == "CANCELLED":
                    removed.append(value)
        for itemToRemove in removed:
            if itemToRemove in values:
                values.remove(itemToRemove)
        if len(values) == 0:
            return None
        name = "givenName"
        customer = "customer"
        lastName = "familyName"
        testingSite = "testingSite"
        siteName = "name"
        testDate = "startTime"
        id = "id"
        for i, value in enumerate(values):
            print(f"{i + 1}: {value[id]} -- {value[customer][name]} {value[customer][lastName]} at {value[testingSite][siteName]} on {value[testDate]}")
        print(f"{i + 2}: None")
        idIndex = int(input("Please choose from the following: ")) -1
        if idIndex == i + 1:
            return None
        return self.getByID(values[idIndex]["id"])
