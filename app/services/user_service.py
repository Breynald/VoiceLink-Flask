# from dal.user_dao import UserDAO
from ..dal.user_dao import UserDAO
from flask_jwt_extended import create_access_token
import uuid

class UserService:
    def __init__(self, user_dao:UserDAO):
        self.__user_dao = user_dao

    def register(self, username, email, password):
        if self.__user_dao.checkRepeatemail(email):
            return {'message': 'Register Failed: Email address already exists.'}, 400
        
        random_uuid = str(uuid.uuid4())
        self.__user_dao.insertNewaccount(random_uuid, username, email, password)
        return {'message': 'Register successfully'}, 200
    
    def login(self, email, password):
        user_uuid = self.__user_dao.checkEmailandPassword(email, password)
        if not user_uuid:
            return {'message': 'Login Failed: The email address or password is incorrect.'}, 400
        
        access_token = create_access_token(identity=user_uuid)
        return {
            'message': 'Login successfully',
            'access_token': access_token
        }, 200
