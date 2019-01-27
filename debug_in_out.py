'''
Function taken from:
https://realpython.com/primer-on-python-decorators/
With additional text that shows current iteration of function
'''

import functools


def debug(func):
    """Print the function signature and return value"""
    i = 1

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        nonlocal i
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"ITERATION {i}: Calling {func.__name__}({signature})",end=' ||| ')
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        i += 1
        return value
    return wrapper_debug
