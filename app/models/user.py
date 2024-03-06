

class User:
    def __init__(self, uuid, username, email, password):
        self.__uuid = uuid
        self.__username = username
        self.__email = email
        self.__password = password

    

    def getUuid(self):
        return self.__uuid
    
    def getUsername(self):
        return self.__username
    
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def setUuid(self, uuid):
        self.__uuid = uuid

    def setUsername(self, username):
        self.__username = username

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password