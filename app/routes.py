from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from app import app, mysql
from flask import jsonify, request
import uuid
from .sql_queries import sql_queries


@app.route('/api/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # receive data from frontend
        data = request.json
        random_uuid = str(uuid.uuid4())
        
        cur = mysql.cursor()
        # check repeat email
        cur.execute(sql_queries['check_repeat_email'], (data['email'],))
        existing_user = cur.fetchone()
        if existing_user:
            cur.close()
            return jsonify({'message': 'Register Failed: Email address already exists.'}), 400
        else:
            #insert new account
            cur.execute(sql_queries['insert_new_account'],
                        (random_uuid, data['username'], data['email'], data['password']))
            cur.close()
            print("Received register data from frontend:", data)
            return jsonify({'message': 'Register successfully'})

    

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # receive data from frontend
        data = request.json
        
        cur = mysql.cursor()
        # check email and password
        cur.execute(sql_queries['check_email_and_password'], (data['email'], data['password']))
        existing_uuid = cur.fetchone()
        cur.close()
        if not existing_uuid:
            return jsonify({'message': 'Login Failed: User not exist or password incorrect.'}), 400
        else:
            access_token = create_access_token(identity=existing_uuid)
            # print("Received login data from frontend:", data)
            return jsonify({
                'message': 'Login successfully',
                'access_token': access_token
            }), 200

# 受保护端点
@app.route('/api/autologin', methods=['POST'])
@jwt_required()  # 这个装饰器要求访问该端点时需要验证 JWT token
def autologin():
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    return jsonify(logged_in_as=current_user), 200

