import os
from flask import Flask
from flask_socketio import SocketIO
from flask_compress import Compress

from flask_cors import CORS, cross_origin
import eventlet
eventlet.monkey_patch()

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None


app_tanks = Flask(__name__, template_folder='/var/www/tanks/', static_folder='/var/www/tanks/static')

Compress(app_tanks)
app_tanks.config["SECRET_KEY"] = "tanks!"

CORS(app_tanks, resources={r"/*": {"origins": "*", 'supports_credentials': 'true'}})
socketio = SocketIO(app_tanks, cors_allowed_origins="*")
# else:
#     socketio = SocketIO(app_tanks, async_mode=async_mode, cors_allowed_origins="*", message_queue='redis://')
