from urllib.request import urlopen
def page(url):
    def get():
        return urlopen(url).read()
    return get


tieba = page('http://www.baidu.com')
print(tieba.__closure__[0].cell_contents)