class User:
    def __init__(self, userData) -> None:
        self.id = userData["id"]
        self.givenName = userData["givenName"]
        self.authorisations = []
        if userData["isCustomer"]: self.authorisations.append(1)
        if userData["isReceptionist"]: self.authorisations.append(2)
        if userData["isHealthcareWorker"]: self.authorisations.append(3)
