from API_Handlers.API_Caller import APICaller
import json

class UserCaller(APICaller):
    def __init__(self) -> None:
        self.jwt = None
        user = {
            "id": "string",
            "givenName": "string",
            "familyName": "string",
            "userName": "string",
            "phoneNumber": "string",
            "isCustomer": True,
            "isReceptionist": True,
            "isHealthcareWorker": True,
            "bookings": [
            {
                "id": "string",
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
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "additionalInfo": {}
                },
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "startTime": "2022-04-28T05:23:45.474Z",
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
                    "datePerformed": "2022-04-28T05:23:45.474Z",
                    "dateOfResults": "2022-04-28T05:23:45.474Z",
                    "createdAt": "2022-04-28T05:23:45.474Z",
                    "updatedAt": "2022-04-28T05:23:45.474Z",
                    "additionalInfo": {}
                }
                ],
                "notes": "string",
                "additionalInfo": {}
            }
            ],
            "testsTaken": [
            {
                "id": "string",
                "type": "string",
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
                    "createdAt": "2022-04-28T05:23:45.474Z",
                    "updatedAt": "2022-04-28T05:23:45.474Z",
                    "additionalInfo": {}
                },
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "startTime": "2022-04-28T05:23:45.474Z",
                "smsPin": "string",
                "status": "string",
                "notes": "string",
                "additionalInfo": {}
                },
                "result": "string",
                "status": "string",
                "notes": "string",
                "datePerformed": "2022-04-28T05:23:45.474Z",
                "dateOfResults": "2022-04-28T05:23:45.474Z",
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "additionalInfo": {}
            }
            ],
            "testsAdministered": [
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
                    "createdAt": "2022-04-28T05:23:45.474Z",
                    "updatedAt": "2022-04-28T05:23:45.474Z",
                    "additionalInfo": {}
                },
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "startTime": "2022-04-28T05:23:45.474Z",
                "smsPin": "string",
                "status": "string",
                "notes": "string",
                "additionalInfo": {}
                },
                "result": "string",
                "status": "string",
                "notes": "string",
                "datePerformed": "2022-04-28T05:23:45.474Z",
                "dateOfResults": "2022-04-28T05:23:45.474Z",
                "createdAt": "2022-04-28T05:23:45.474Z",
                "updatedAt": "2022-04-28T05:23:45.474Z",
                "additionalInfo": {}
            }
            ],
            "additionalInfo": {"notifications" : []}
        }
        return super().__init__("/user", user)


    def login(self, username, password):
        import requests
        response  = requests.post(
        url= f"{self.urlBase}/login",
        headers={ 'Authorization': self.apiKey },
        params={ 'jwt': 'true' }, 
        data={
            'userName': username,
            'password': password 
        })
        if response.status_code == 200:
            self.jwt = json.loads(response.text)["jwt"]
        self.status = response.status_code
        
    def select(self, filter = None):
        values = self.get()
        name = "givenName"
        lastName = "familyName"
        id = "id"
        for i, value in enumerate(values):
            print(f"{i + 1}: {value[name]} {value[lastName]}")
        idIndex = int(input("Please choose from the following: ")) -1
        return self.getByID(values[idIndex]["id"])
