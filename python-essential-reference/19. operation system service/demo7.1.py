import logging

log = logging.getLogger('log.' + __name__)
log.critical('can not connect %s at port %d', host, port)
log.setLevel(logging.INFO)

params = {
    'host': 'www.tian.com',
    'port': 80
}

log.critical('can not connect %(host)s at port %(port)d', params)