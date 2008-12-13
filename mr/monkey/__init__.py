from copy import copy
from sys import modules
import warnings
import inspect
import sha


class MonkeyException(Exception):
    """An exception for errors on applying monkey patches."""


class MonkeyWarning(RuntimeWarning):
    """A warning for applied monkey patches."""

class MonkeySignatureWarning(RuntimeWarning):
    """A warning about missing signatures for monkey patches."""


def funcinfo(func):
    """ returns the container (class or module) and name of a function """
    if hasattr(func, 'im_class'):
        container = func.im_class
        dottedname = '.'.join((container.__module__,
                               container.__name__,
                               func.__name__))
        return container, dottedname, func.__name__
    else:
        container = modules[func.__module__]
        dottedname = '.'.join((func.__module__, func.__name__))
        return container, dottedname, func.__name__


def verify(target, signatures):
    if signatures is None:
        return
    container, dottedname, funcname = funcinfo(target)
    try:
        code = inspect.getsource(target)
    except IOError:
        code = target.func_code
    signature = sha.new(code).hexdigest()

    if signature not in signatures:
        warnings.warn(
            "%s is not a valid signature for %s." % (signature, dottedname),
            MonkeySignatureWarning,
            stacklevel=3)


def replace(target, replacement, signatures=()):
    verify(target, signatures)
    container, dottedname, funcname = funcinfo(target)
    if getattr(target, '__mr_monkey_info__', False):
        raise MonkeyException("Trying to apply monkey patch %s twice." %
                              dottedname)
    else:
        warnings.warn('Wrapping %s.' % dottedname,
                      MonkeyWarning,
                      stacklevel=2)
    replacement.__doc__ = target.__doc__
    info = replacement.__mr_monkey_info__ = dict(
        original = target,
    )
    setattr(container, funcname, replacement)


def wrap(target, handler, signatures=()):
    verify(target, signatures)
    def wrapper(*args, **kwargs):
        return handler(target, *args, **kwargs)
    replace(target, wrapper)
