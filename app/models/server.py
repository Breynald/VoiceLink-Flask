
class Server:
    def __init__(self, serverid, servername, serverpassword, serverip, serverport):
        self.__serverid = serverid
        self.__servername = servername
        self.__serverpassword = serverpassword
        self.__serverip = serverip
        self.__serverport = serverport

    def getServerid(self):
        return self.__serverid
    
    def getServername(self):
        return self.__servername
    
    def getServerpassword(self):
        return self.__serverpassword
    
    def getServerip(self):
        return self.__serverip
    
    def getServerport(self):
        return self.__serverport
    
    def setServerid(self, serverid):
        self.__serverid = serverid

    def setServername(self, servername):
        self.__servername = servername

    def setServerpassword(self, serverpassword):
        self.__serverpassword = serverpassword

    def setServerip(self, serverip):
        self.__serverip = serverip

    def setServerport(self, serverport):
        self.setServerport = serverport

