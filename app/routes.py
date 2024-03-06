from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, user_service
from flask import jsonify, request


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    message, status_code = user_service.register(data['username'], data['email'], data['password'])
    return message, status_code
    

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    response, status_code = user_service.login(data['email'], data['password'])
    return response, status_code


@app.route('/api/autologin', methods=['POST'])
@jwt_required()  # 这个装饰器要求访问该端点时需要验证 JWT token
def autologin():
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    return jsonify(logged_in_as=current_user), 200

