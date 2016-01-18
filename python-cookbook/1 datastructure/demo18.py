from collections import namedtuple

Host = namedtuple('Host', ['hostname', 'port'])
h = Host('127.0.0.1', 3000)

print(h.hostname)
print(h.port)

print(h._asdict())