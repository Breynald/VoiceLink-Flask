
class Channel:
    def __init__(self, serverid, channelid, channelname, channelpassword, maxplayer:int, currentcount:int, ):
        self.__serverid = serverid
        self.__channelid = channelid
        self.__channelname = channelname
        self.__channelpassword = channelpassword
        self.__maxplayer = maxplayer if maxplayer>0 else 0
            
    
    def getServerid(self):
        return self.__serverid

    def getChannelid(self):
        return self.__channelid
    
    def getChannelname(self):
        return self.__channelname
    
    def getChannelpassword(self):
        return self.__channelpassword
    
    def getMaxplayer(self):
        return self.__maxplayer
    
    def setServerid(self, serverid):
        self.__serverid = serverid

    def setChannelid(self, channelid):
        self.__channelid = channelid

    def setChannelname(self, channelname):
        self.__channelname = channelname

    def setChannelpassword(self, channelpassword):
        self.__channelpassword = channelpassword
    
    def setMaxplayer(self, maxplayer:int):
        self.__maxplayer = maxplayer
        