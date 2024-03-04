from datetime import timedelta
from app import app, mysql
from flask import jsonify, request, session
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
            session['uuid'] = str(existing_uuid[0]);
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)
            print(session)
            # print("Received login data from frontend:", data)
            print(session['uuid'])
            return jsonify({
                'message': 'Login successfully',
                'sessionuuid': session['uuid']
            }), 200

    

@app.route('/api/autologin', methods=['POST'])
def autologin():
    if request.method == 'POST':
        # receive data from frontend
        session_id = request.json['sessionId']
        
        if not session_id:
            return jsonify({'message': 'Auto Login Failed: No session.'}), 400
        elif session.sid != session_id:
            return jsonify({'message': 'Auto Login Failed: Invalid session.'}), 400
        else:
            session.update(session_id)
            session.permanent = True
            app.permanent_session_lifetime = timedelta(days=7)
            return jsonify({
                'message': 'Auto Login successfully'
            }), 200

