#!/usr/bin/env python
# -*- coding: utf-8 -*
from flask import request

from app.conf import socketio

from utility.logger import Logger

from storage.fields import only_field

logger = Logger()

@socketio.on("connect", namespace="/field")
def connect():
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client connect ","/field",request.sid)
    # only_field.add_user(request.sid)

@socketio.on("disconnect", namespace="/field")
def disconnect():
    """
    Функция вызывается при подключении к серверу
    """
    logger.debug("Client disconnect ","/field",request.sid)
    # only_field.delete_user(request.sid)