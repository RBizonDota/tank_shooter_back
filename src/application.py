#!/usr/bin/env python
# -*- coding: utf-8 -*

from config.const import HOST, PORT

import handlers.field
import handlers.tank_control

from processing.control_thread import StreamBackground 

if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     if "version" in sys.argv:
    #         print("VERSION={}".format(VERSION))
    #     sys.exit(0)

    # Запуск сервиса
    from app.conf import app_tanks, socketio

    socketio.start_background_task(StreamBackground().background_thread)
    socketio.run(app_tanks, debug=True, host=HOST, port=PORT)
