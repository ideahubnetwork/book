""" 
返回一个代理对象委托方法调用一个父类或者邻类。这是有用的对于访问在类中已经被重写了的方法。搜索顺序与使用getattr()一致。

__mro__属性列出了getattr与super的搜索顺序。这个属性是动态的而且能被改变当继承层更新的时候。

如果第二参数被省略，超类返回的是未绑定的。如果第二参数是一个实例，必须满足 isinstance(obj, type)。如果第二个参数是一个class，必须满足issubclass(type2, type)。

对于super，有两个典型的用例。在一个带有单个继承的类层次中，super可以被用来指代没有明确命名的父类，因此使代码更加可维持。在其他编程语言中，

第二个用例是在一个动态执行环境中支持合作多继承。

"""

class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Cant delete attribute')


class SubPerson(Person):

    @property
    def name(self):
        print('getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('xiange')
print(s.name)

