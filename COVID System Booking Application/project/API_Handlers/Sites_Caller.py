from API_Handlers.API_Caller import APICaller


class SitesCaller(APICaller):
    def __init__(cls) -> None:
        site = {
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
            "bookings": [
                {
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
                    "createdAt": "2022-04-28T04:48:43.784Z",
                    "updatedAt": "2022-04-28T04:48:43.784Z",
                    "startTime": "2022-04-28T04:48:43.784Z",
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
                            "datePerformed": "2022-04-28T04:48:43.784Z",
                            "dateOfResults": "2022-04-28T04:48:43.784Z",
                            "createdAt": "2022-04-28T04:48:43.784Z",
                            "updatedAt": "2022-04-28T04:48:43.784Z",
                            "additionalInfo": {}
                        }
                    ],
                    "notes": "string",
                    "additionalInfo": {}
                }
            ],
            "createdAt": "2022-04-28T04:48:43.784Z",
            "updatedAt": "2022-04-28T04:48:43.784Z",
            "additionalInfo": {
                "facilityType": "string",
                "facilityStatus": "string",
                "waitingTime": "string",
                "onSiteBooking": True,
                "changes" : [],
            }
        }
        return super().__init__("/testing-site", site)

    def select(self, filter = None):
        values = self.get()
        name = "name"
        id = "id"
        for i, value in enumerate(values):
            print(f"{i + 1}: {value[name]}")
        idIndex = int(input("Please choose from the following sites: ")) -1
        return self.getByID(values[idIndex]["id"])

        