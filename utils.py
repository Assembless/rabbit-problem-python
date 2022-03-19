import threading

def set_interval(func, sec):
    """Set an interval to call a function."""
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t