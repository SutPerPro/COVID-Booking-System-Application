from API_Handlers.API_Caller import APICaller


class CovidTestCaller(APICaller):
    def __init__(cls) -> None:
        covidTest = {
            "id": "string",
            "type": "PCR",
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
            "booking": {
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
                    "createdAt": "2022-04-28T14:42:56.951Z",
                    "updatedAt": "2022-04-28T14:42:56.951Z",
                    "additionalInfo": {
                        "facilityType": "string",
                        "facilityStatus": "string",
                        "waitingTime": "string",
                        "onSiteBooking": True
                    }
                },
                "createdAt": "2022-04-28T14:42:56.951Z",
                "updatedAt": "2022-04-28T14:42:56.951Z",
                "startTime": "2022-04-28T14:42:56.951Z",
                "smsPin": "string",
                "status": "string",
                "notes": "string",
                "additionalInfo": {}
            },
            "result": "POSITIVE",
            "status": "string",
            "notes": "string",
            "datePerformed": "2022-04-28T14:42:56.951Z",
            "dateOfResults": "2022-04-28T14:42:56.951Z",
            "createdAt": "2022-04-28T14:42:56.951Z",
            "updatedAt": "2022-04-28T14:42:56.951Z",
            "additionalInfo": {}
        }
        return super().__init__("/covid-test", covidTest)


    def select(self):
        pass