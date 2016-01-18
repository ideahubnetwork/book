class MyClsMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        def clsm(*args):
            return self.func(cls, *args)
        return clsm

class Point:
    @staticmethod
    def get(a = 1):
        return 3, 4

    @MyClsMethod
    def getc(cls, a, b, c):
        return 3, 4

print(Point.get())
print(Point.getc(1,2,3))

p = Point()
print(p.get())
print(p.getc(1,2,3))