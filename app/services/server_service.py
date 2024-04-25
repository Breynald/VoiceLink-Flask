from ..dal.server_dao import ServerDAO
import uuid

class ServerService:
    def __init__(self, server_dao:ServerDAO):
        self.__server_dao = server_dao

    def createServer(self, servername, serverpassword, serverip, serverport, avatarname, userid):
        serverid = str(uuid.uuid4())
        avatarurl = 'http://127.0.0.1:5000/static/img/' + avatarname
        if self.__server_dao.insertNewserver(serverid, servername, serverpassword, serverip, serverport, avatarurl):
            self.joinServer(userid, serverid, serverpassword)
            return {'message': 'Create server successfully.'}, 200
        else:
            return {'message': 'Create server failed, try again later.'}, 400
    
    def joinServer(self, userid, serverid, serverpassword):
        userinserver = self.__server_dao.checkUserinServer(userid, serverid)
        if userinserver is not None and len(userinserver) > 0:
            return { 'message': 'Already in this server.' }, 400

        if self.__server_dao.checkServerPublic(serverid):
            if self.__server_dao.addUsertoserver(userid, serverid):
                return { 'message': 'Join server successfully.'}, 200
            else:
                return { 'message': 'Join server failed, try again later.'}, 400

        if self.__server_dao.checkPassword(serverid, serverpassword):
            if self.__server_dao.addUsertoserver(userid, serverid):
                return { 'message': 'Join server successfully.'}, 200
            else:
                return { 'message': 'Join server failed, try again later.'}, 400
        else:
            return {'message': 'The server password is incorrect.'}, 400

    def getServerlist(self, userid):
        serveridlist = self.__server_dao.getServeridlist(userid)
        serverlist = []
        if len(serveridlist) > 0:
            for serverid in serveridlist:
                    data = self.__server_dao.getServer(serverid[0])
                    serverlist.append({
                        'serverid': data[0],
                        'servername': data[1],
                        'serverip': data[3],
                        'serverport': data[4],
                        'avatarurl': data[5]
                    })
            return {
                'message': 'Get server list successfully.',
                'serverlist': serverlist
            }, 200
        else:
            return {
                'message': 'Get no server.',
                'serverlist': None
            }, 404
        
    def getServer(self, serverid):
        data = self.__server_dao.getServer(serverid)
        if data is not None:
            return {
                'message': 'Get server successfully.',
                'server': {
                    'serverid': data[0],
                    'servername': data[1],
                    'serverip': data[3],
                    'serverport': data[4],
                    'avatarurl': data[5]
                }
            }, 200
        else:
            return {
                'message': 'Get no server.'
            }, 404

    def getChannellist(self, serverid):
        datas = self.__server_dao.getChannellist(serverid)
        if len(datas) > 0:
            channellist = []
            for data in datas:
                channellist.append({
                    'channelid': data[0],
                    'channelname': data[2],
                    'channelpassword': data[3],
                    'maxplayer': data[4],
                    'currentplayer': data[5]
                })
            return {
                'message': 'Get channel list successfully.',
                'channellist': channellist
            }, 200
        else:
            return {
                'message': 'Get no channel.',
                'channellist': None
            }, 404


    def getChanneluserscount(self, serverid, channelid):
        data = self.__server_dao.getChanneluserscount(serverid, channelid)
        if data is not None:
            return data[0]
        else:
            return -1

    def setChanneluserscount(self, serverid, channelid, count):
        if self.__server_dao.setChanneluserscount(serverid, channelid, count):
            return True
        else:
            return False
        
    def addChannel(self, serverid, channelname, channelpassword, maxplayer):
        if self.__server_dao.insertNewchannel(serverid, channelname, channelpassword, maxplayer):
            return {'message': 'Add channel successfully.'}, 200
        else:
            return {'message': 'Add channel failed, try again later.'}, 400

    def delChannel(self, serverid, channelid):
        if self.__server_dao.delChannel(serverid, channelid):
            return {'message': 'Del channel successfully.'}, 200
        else:
            return {'message': 'Del channel failed, try again later.'}, 400
        

    def saveAvatar(self, file_obj, file_name):
        import os
        try:
            parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            save_path = os.path.join(parent_parent_dir, 'static', 'img', file_name)
            file_obj.save(save_path)
            return {
                'message': 'Save avatar successfully.'
            }, 200
        except Exception as e:
            print(f"An error occurred: {e}")
            return {
                'message': 'Save avatar failed.'
            }, 400
        

    def searchServer(self, servername):
        datas = self.__server_dao.searchServer(servername)
        if len(datas)>0:
            serverlist = []
            for data in datas:
                serverlist.append({
                    'serverid': data[0],
                    'servername': data[1],
                    'serverpassword': data[2],
                    'avatarurl': data[5]
                })
            return {
                'message': 'Search server successfully.',
                'serverlist': serverlist
            }, 200
        else:
            return {
                'message': 'Search no server.'
            }, 404