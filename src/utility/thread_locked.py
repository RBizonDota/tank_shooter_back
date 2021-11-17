from threading import Lock

thread_lock = Lock()


def thread_locked(function_to_decorate):
    """
    Декоратор блокировки потока
    """
    def wrapper(*args):
        thread_lock.acquire()
        returned = function_to_decorate(*args)
        thread_lock.release()
        return returned
    return wrapper
