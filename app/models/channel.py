
class Channel:
    def __init__(self, channelid, channelname, channelpassword, maxplayer):
        self.__channelid = channelid
        self.__channelname = channelname
        self.__channelpassword = channelpassword
        self.__maxplayer = maxplayer
    
    def getChannelid(self):
        return self.__channelid
    
    def getChannelname(self):
        return self.__channelname
    
    def getChannelpassword(self):
        return self.__channelpassword
    
    def getMaxplayer(self):
        return self.__maxplayer
    
    def setChannelid(self, channelid):
        self.__channelid = channelid

    def setChannelname(self, channelname):
        self.__channelname = channelname

    def setChannelpassword(self, channelpassword):
        self.__channelpassword = channelpassword
    
    def setMaxplayer(self, maxplayer):
        self.__maxplayer = maxplayer
        