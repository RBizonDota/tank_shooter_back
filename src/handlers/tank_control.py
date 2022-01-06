#!/usr/bin/env python
# -*- coding: utf-8 -*
from flask import request

from app.conf import socketio

from utility.logger import Logger

from storage.fields import only_field

logger = Logger()

@socketio.on("connect", namespace="/tank_control")
def connect():
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client connect ","/tank_control",request.sid)
    # return tank

@socketio.on("disconnect", namespace="/tank_control")
def disconnect():
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client disconnect ","/tank_control",request.sid)
    only_field.delete_tank(request.sid)

@socketio.on("tank_control", namespace="/tank_control")
def tank_control(message=None):
    """
    Функция вызывается при передаче серверу управляющего воздействия пользователя
    """
    logger.debug("Client user control ","/tank_control",request.sid, message)
    if message:
        only_field.set_user_control(request.sid, message)

@socketio.on('init', namespace='/tank_control')
def foo(message):
    tank = only_field.create_tank(request.sid)

    # socketio.emit(tank)
    print("EMITING to", )
    # socketio.emit('your_tank', tank, namespace='/tank_control', room=request.sid)
    return tank

