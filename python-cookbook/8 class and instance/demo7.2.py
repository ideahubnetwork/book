class Base:
    def __init__(self):
        print('base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('a.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('b.__init__')

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('c.__init__')

C()
