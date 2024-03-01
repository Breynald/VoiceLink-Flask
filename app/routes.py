from app import app, mysql
from flask import jsonify, request
import uuid
from .sql_queries import sql_queries

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     # 处理获取数据的逻辑，例如从数据库中获取数据
#     data = {'message': 'Hello from Flask!'}
#     return jsonify(data)

# @app.route('/api/send_data', methods=['POST'])
# def send_data():
#     # 处理接收前端发送的数据并进行相应操作的逻辑
#     request_data = request.get_json()
#     # 处理接收到的数据
#     return jsonify({'message': 'Data received successfully!'})


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
        existing_user = cur.fetchone()
        cur.close()
        if not existing_user:
            return jsonify({'message': 'Login Failed: User not exist.'}), 400
        else:
            print("Received login data from frontend:", data)
            return jsonify({'message': 'Login successfully'})


