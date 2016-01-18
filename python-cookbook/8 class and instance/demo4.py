import sys


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


date = [Date(2015, 9, 13) for i in range(100)]
print(sys.getsizeof(date))
