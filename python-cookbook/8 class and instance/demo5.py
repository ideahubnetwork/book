class Person:
    def __init__(self):
        self._age = 21

    def _run(self):
        print('run')

    def __eat(self):
        pass

class Tian(Person):
    def __init__(self):
        super().__init__()
        self._age = 22

    def _run(self):
        super()._run()
        print('run--run')

    def __eat(self):
        pass


p = Person()
print(dir(p))

t = Tian()
print(dir(t))
t._run()