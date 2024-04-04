from ..dal.server_dao import ServerDAO
import uuid

class ServerService:
    def __init__(self, server_dao:ServerDAO):
        self.__server_dao = server_dao

    def createServer(self, servername, serverpassword, serverip, serverport):
        serverid = str(uuid.uuid4())
        if self.__server_dao.insertNewserver(serverid, servername, serverpassword, serverip, serverport):
            return {'message': 'Create server successfully.'}, 200
        else:
            return {'message': 'Create server failed, try again later.'}, 400
    
    def joinServer(self, userid, serverid, serverpassword):
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
                        'serverport': data[4]
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
                    'serverport': data[4]
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
                    'channelindex': data[2],
                    'channelname': data[3],
                    'channelpassword': data[4],
                    'maxplayer': data[5],
                    'currentplayer': data[6]
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
