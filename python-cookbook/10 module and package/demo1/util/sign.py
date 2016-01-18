# coding: utf-8
import pkgutil

class SignBefore(object):
    def __init__(self):
        pass

    def __str__(self):
        return 'this is a sign'


    def __repr__(self):
        return 'object sign'


class SignAfter(object):
    def __init__(self):
        pass

    def __str__(self):
        return 'this is a sign'


    def __repr__(self):
        return 'object sign'

def set_cookie():
    with open('text.txt', 'a') as f:
        f.write('hello, world')


def get_cookie():
    # try:
    #     with open('text.txt') as f:
    #         print(f.read())
    # # python中异常处理为as
    # except IOError as e:
    #     print(e)
    return pkgutil.get_data(__package__, 'text.txt')

info = 'package:{}\nfile:{}'.format(__package__, __file__)
if __name__ == '__main__':
    get_cookie()


