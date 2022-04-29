#contains code for debug printing and flag
import inspect

_DEBUG = False
def printd(s):
    if(_DEBUG):
        print("DEBUG::%s() -> %s" % (inspect.stack()[1].function, s))
