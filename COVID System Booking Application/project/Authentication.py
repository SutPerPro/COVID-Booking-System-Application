from user import User
class Authentication:
    
    @staticmethod
    def verifyLogin(username = None, password = None)->User:
        if (username is None and password is None):
            username = input("Username: ")
            password = input("Password: ")
        return Authentication.__PostLogin(username, password)


    @staticmethod
    def __PostLogin(username : str, password : str)->User:
        from API_Handlers.User_Caller import UserCaller
        response = UserCaller()
        response.login(username, password)
        if response.status == 200:
            users = response.get()
            for user in users:
                if user["userName"] == username:
                    return user
            return None
        