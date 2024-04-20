from app import app, socketio
from app.routes import *

if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app)
