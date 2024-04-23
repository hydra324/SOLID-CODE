"""
pythonic singleton class
"""

from typing import Any


class Singleton(type):
    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]
    
class Logger(metaclass=Singleton):
    def log(self, log):
        print(log)

logger1 = Logger()
print(logger1)
logger2 = Logger()
print(logger2)


class MyClass:
    @staticmethod
    def do_something(text):
        print(text)

MyClass.do_something("hello")