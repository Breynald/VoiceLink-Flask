from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, socketio, user_service, server_service
from flask import jsonify, request
from flask_socketio import emit


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

@app.route('/api/createserver', methods=['POST'])
def createserver():
    data = request.json
    response, status_code = server_service.createServer(data['servername'], data['serverpassword'], data['serverip'], data['serverport'], data['avatarname'], data['userid'])
    return response, status_code

@app.route('/api/joinserver', methods=['POST'])
def joinserver():
    data = request.json
    response, status_code = server_service.joinServer(data['userid'], data['serverid'], data['serverpassword'])
    return response, status_code

@app.route('/api/autologin', methods=['POST'])
@jwt_required()  # 这个装饰器要求访问该端点时需要验证 JWT token
def autologin():
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    return jsonify(logged_in_as=current_user), 200

@app.route('/api/getserverlist', methods=['POST'])
def getserverlist():
    data = request.json
    response, status_code = server_service.getServerlist(data['userid'])
    return response, status_code

@app.route('/api/getserver', methods=['POST'])
def getserver():
    data = request.json
    response, status_code = server_service.getServer(data['serverid'])
    return response, status_code

@app.route('/api/getchannellist', methods=['POST'])
def getchannellist():
    data = request.json
    response, status_code = server_service.getChannellist(data['serverid'])
    return response, status_code

@app.route('/api/getuser', methods=['POST'])
def getuser():
    data = request.json
    response, status_code = user_service.getUser(data['userid'])
    return response, status_code

@app.route('/api/setusername', methods=['POST'])
def setusername():
    data = request.json
    response, status_code = user_service.setUsername(data['userid'], data['username'])
    return response, status_code

@app.route('/api/addchannel', methods=['POST'])
def addchannel():
    data = request.json
    response, status_code = server_service.addChannel(data['serverid'], data['channelname'], data['channelpassword'], data['maxplayer'])
    return response, status_code

@app.route('/api/delchannel', methods=['POST'])
def delchannel():
    data = request.json
    response, status_code = server_service.delChannel(data['serverid'], data['channelid'])
    return response, status_code

@app.route('/api/saveavatar', methods=['POST'])
def saveavatar():
    file_obj = request.files.get('file')
    file_name = request.form.get('filename')
    response, status_code = server_service.saveAvatar(file_obj, file_name)
    return response, status_code

@app.route('/api/searchserver', methods=['POST'])
def searchserver():
    data = request.json
    response, status_code = server_service.searchServer(data['servername'])
    return response, status_code



@socketio.on('joinchannel')
def joinchannel(data):
    serverid = data['serverid']
    channelid = data['channelid']
    
    current_user_count = server_service.getChanneluserscount(serverid, channelid)

    server_service.setChanneluserscount(serverid, channelid, current_user_count+1)

    emit('channel_users_count', {'serverid': serverid, 'channelid': channelid, 'count': current_user_count + 1}, broadcast=True)


@socketio.on('leavechannel')
def leavechannel(data):
    serverid = data['serverid']
    channelid = data['channelid']
    
    current_user_count = server_service.getChanneluserscount(serverid, channelid)

    server_service.setChanneluserscount(serverid, channelid, current_user_count-1)

    emit('channel_users_count', {'serverid': serverid, 'channelid': channelid, 'count': current_user_count - 1}, broadcast=True)

