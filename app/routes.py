from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, user_service, server_service
from flask import jsonify, request


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    response, status_code = user_service.register(data['username'], data['email'], data['password'])
    return response, status_code

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    response, status_code = user_service.login(data['email'], data['password'])
    return response, status_code

@app.route('api/createserver', method=['POST'])
def createserver():
    data = request.json
    response, status_code = server_service.createServer(data['servername'], data['serverpassword'], data['serverip'], data['serverport'])
    return response, status_code

@app.route('/api/joinserver', method=['POST'])
def joinserver():
    data = request.json
    response, status_code = server_service.joinServer(data['userid'], data['serverid'], data['serverpassword'])
    return response, status_code

@app.route('/api/autologin', methods=['POST'])
@jwt_required()  # 这个装饰器要求访问该端点时需要验证 JWT token
def autologin():
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    return jsonify(logged_in_as=current_user), 200

