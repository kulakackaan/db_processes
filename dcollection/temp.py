import functools
import logging

def log_error(logger):
    def decorated(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                if logger:
                    logger.exception(e)
                raise
        return wrapped
    return decorated

logger = logging.getLogger()
@log_error(logger)
def f():
    return 1/0

f()