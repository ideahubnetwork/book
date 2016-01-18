# coding: utf-8

"""8.2 自定义字符串的输出格式"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        _formats = {
            'ymd': '{0.year}-{0.month}-{0.day}',
            'ymd2': '{0.year}/{0.month}/{0.day}'
        }
        return _formats[code].format(self)


date = Date(2015, 12, 6)
print(format(date))