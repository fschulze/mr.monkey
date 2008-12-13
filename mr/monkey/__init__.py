from copy import copy
from sys import modules


def funcinfo(func):
    """ returns the container (class or module) and name of a function """
    if hasattr(func, 'im_class'):
        container = func.im_class
        dottedname = '.'.join((container.__module__,
            container.__name__, func.__name__))
        return container, dottedname, func.__name__
    else:
        container = modules[func.__module__]
        dottedname = '.'.join((func.__module__, func.__name__))
        return container, dottedname, func.__name__


def replace(target, replacement):
    container, dottedname, funcname = funcinfo(target)
    replacement.__doc__ = target.__doc__
    info = replacement.__mr_monkey_info__ = dict(
        original = target,
    )
    setattr(container, funcname, replacement)


def wrap(target, handler):
    def wrapper(*args, **kwargs):
        return handler(target, *args, **kwargs)
    replace(target, wrapper)
