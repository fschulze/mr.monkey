

def foo(result=None):
    if result is not None:
        return result
    else:
        return 1, 2, 3

class ClassicBlubb:
    def bar(self, result=None):
        if result is not None:
            return result
        else:
            return 1, 2, 3

class NewStyleBlubb(object):
    def bar(self, result=None):
        if result is not None:
            return result
        else:
            return 1, 2, 3
