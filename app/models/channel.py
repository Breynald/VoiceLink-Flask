
class Channel:
    def __init__(self, serverid, channelindex, channelname, channelpassword, maxplayer:int, currentplayer:int):
        self.__serverid = serverid
        self.__channelindex = channelindex
        self.__channelname = channelname
        self.__channelpassword = channelpassword
        self.__maxplayer = maxplayer if maxplayer>0 else 0
        self.__currentplayer = currentplayer
    
    def getServerid(self):
        return self.__serverid

    def getChannelindex(self):
        return self.__channelindex
        
    def getChannelname(self):
        return self.__channelname
    
    def getChannelpassword(self):
        return self.__channelpassword
    
    def getMaxplayer(self):
        return self.__maxplayer
    
    def getCurrentplayer(self):
        return self.__currentplayer

    def setServerid(self, serverid):
        self.__serverid = serverid

    def setChannelid(self, channelindex):
        self.__channelindex = channelindex

    def setChannelname(self, channelname):
        self.__channelname = channelname

    def setChannelpassword(self, channelpassword):
        self.__channelpassword = channelpassword
    
    def setMaxplayer(self, maxplayer:int):
        self.__maxplayer = maxplayer
        
    def setCurrentplayer(self, currentplayer:int):
        self.__currentplayer = currentplayer