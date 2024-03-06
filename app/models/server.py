from channel import Channel

class Server:
    def __init__(self, serverid, servername, serverpassword, channellist=None):
        self.__serverid = serverid
        self.__servername = servername
        self.__serverpassword = serverpassword
        self.__channellist = channellist if channellist is not None else []

    def getServerid(self):
        return self.__serverid
    
    def getServername(self):
        return self.__servername
    
    def getServerpassword(self):
        return self.__serverpassword
    
    def getChannellist(self):
        return self.__channellist
    
    def setServerid(self, serverid):
        self.__serverid = serverid

    def setServername(self, servername):
        self.__servername = servername

    def setServerpassword(self, serverpassword):
        self.__serverpassword = serverpassword

    def addChannel(self, channel:Channel):
        self.__channellist.append(channel)

    def delChannel(self, channelid):
        for channel in self.__channellist:
            if channel.getChannelid() == channelid:
                self.__channellist.remove(channel)

