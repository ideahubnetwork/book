""" 创建可管理的属性，使用property
"""


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        formats = {
            '': '{}/{}/{}',
            '-': '{}-{}-{}',
        }
        return formats[code].format(self.year, self.month, self.day)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if value < 1 or value > 12:
            raise ValueError('month must be in 1..12')
        self._month = value

date = Date(2015, 12, 23)
print(dir(date))
print(format(date, ''))
