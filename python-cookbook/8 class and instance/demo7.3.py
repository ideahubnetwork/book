class Base:

    def __init__(self):
        print('base.__init__')


class A(Base):

    def __init__(self):
        super().__init__()
        print('a.__init__')


class B(Base):

    def __init__(self):
        super().__init__()
        print('b.__init__')


class C(A, B):

    def __init__(self):
        super().__init__()
        print('c.__init__')

C()
