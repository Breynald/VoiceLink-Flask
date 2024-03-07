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


        
