# 调用父类中的方法


class A:

    def spam(self):
        print('a.spam')


class B(A):

    def spam(self):
        super().spam()
        print('b.spam')

b = B()
b.spam()
