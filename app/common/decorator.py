# -*- coding = utf-8 -*-
import logging
import logging.config
import time
from functools import wraps


def exec_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.time()
        co = func.__code__
        co_name = co.co_name
        resp = func(*args, **kwargs)

        message = "[func|{0}][exec_time|{1}]".format(co_name, time.time() - t)
        logging.info(message)

        return resp
    return wrapper
