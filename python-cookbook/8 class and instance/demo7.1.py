""" error 重复引用"""

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('-'):
            super().__setattr__(name, value)
        return setattr(self._obj, name, value)

class A:
    def __init__(self):
        self.a = 10


obj = A()
p = Proxy(obj)