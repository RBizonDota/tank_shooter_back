from config.const import LOG_LEVEL, LOG_LEVEL_DEBUG, LOG_LEVEL_INFO, LOG_LEVEL_WARN, LOG_LEVEL_ERROR

LOG_LEVEL_DEBUG_MESSAGE = "[ DEBUG ]"
LOG_LEVEL_INFO_MESSAGE  = "[ INFO  ]"
LOG_LEVEL_WARN_MESSAGE  = "[ WARN  ]"
LOG_LEVEL_ERROR_MESSAGE = "[ ERROR ]"

class Logger:
    def __init__(self, log_level=None):
        self.log_level = log_level or LOG_LEVEL
    
    def debug(self, *args):
        if LOG_LEVEL_DEBUG>=self.log_level:
            print(LOG_LEVEL_DEBUG_MESSAGE, *args)

    def info(self, *args):
        if LOG_LEVEL_INFO>=self.log_level:
            print(LOG_LEVEL_INFO_MESSAGE, *args)
            
    def warn(self, *args):
        if LOG_LEVEL_WARN>=self.log_level:
            print(LOG_LEVEL_WARN_MESSAGE, *args)

    def error(self, *args):
        if LOG_LEVEL_ERROR>=self.log_level:
            print(LOG_LEVEL_ERROR_MESSAGE, *args)