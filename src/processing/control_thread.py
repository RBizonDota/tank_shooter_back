from app.conf import socketio
from utility.thread_locked import thread_locked

from storage.fields import only_field

from processing.control_tanks import control_tanks
from processing.control_bullets import control_bullets

from config.const import CPS, SPEED_MODE

from utility.logger import Logger

logger = Logger(log_level=2)

class StreamBackground:
    """
    :param dict self._streams: информация о потоке вида {stream_id: size, ...}
    """

    def __init__(self):
        self.active = True
        self.fields = [only_field]

    def background_thread(self):
        """
        Фоновая задача для работы цикла отправки настроек на front
        """
        while self.active:
            self.field_control()
            socketio.sleep(1/CPS/SPEED_MODE)
            # print(self._streams)

    def stop(self):
        self.active = False

    @thread_locked
    def field_control(self):
        # try:
        for field in self.fields:
            data_changed = False
            data_changed = control_tanks(field) or data_changed
            data_changed = control_bullets(field) or data_changed

        # if data_changed:
            # send field struct to all clients
            data = field.get_data()
            logger.debug("Sending data to users", data, field.users.keys())
            # for user_id in field.users.keys():
                
            socketio.emit("field_data", field.get_data(), namespace='/field')
        # except Exception as e:
        #     logger.error("Exception while field_control:", e)