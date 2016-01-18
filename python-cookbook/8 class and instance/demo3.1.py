from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, tb):
        self.sock.close()
        self.sock = None


from functools import partial

coon = LazyConnection(('www.python.org', 80))
with coon as s:
    s.send(b'hello, world')
