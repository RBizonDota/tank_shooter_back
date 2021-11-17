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
    only_field.create_tank(request.sid)

@socketio.on("disconnect", namespace="/tank_control")
def disconnect():
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client disconnect ","/tank_control",request.sid)
    only_field.delete_tank(request.sid)

@socketio.on("tank_control", namespace="/tank_control")
def tank_control(message):
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client user control ","/tank_control",request.sid, message)
    only_field.set_user_control(request.sid, message)
