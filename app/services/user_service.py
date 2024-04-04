from ..dal.user_dao import UserDAO
from flask_jwt_extended import create_access_token
import uuid

class UserService:
    def __init__(self, user_dao:UserDAO):
        self.__user_dao = user_dao

    def register(self, username, email, password):
        if self.__user_dao.checkRepeatemail(email):
            return {'message': 'Register Failed: Email address already exists.'}, 400
        
        userid = str(uuid.uuid4())
        if self.__user_dao.insertNewaccount(userid, username, email, password):
            return {'message': 'Register successfully.'}, 200
        else:
            return {'message': 'Register Failed.'}, 400

        
    
    def login(self, email, password):
        userid = self.__user_dao.checkEmailandPassword(email, password)
        if not userid:
            return {'message': 'Login Failed: The email address or password is incorrect.'}, 400
        
        access_token = create_access_token(identity=userid)
        return {
            'message': 'Login successfully.',
            'access_token': access_token,
            'userid': userid[0]
        }, 200
        

    def getUsername(self, userid):
        username = self.__user_dao.getUsername(userid)
        if not username:
            return {'message': 'Get Username Failed.'}, 400
        
        return {
            'message': 'Get Username Successfully.',
            'username': username[0]
        }, 200
