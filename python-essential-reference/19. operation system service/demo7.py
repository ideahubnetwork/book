import logging


logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(levelname)-10s %(asctime)s %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logging.getLogger().addHandler(logging.StreamHandler())

for i in range(1000):
    if i % 10 == 0:
        logging.info(i)
    if i % 100 == 0:
        logging.warning(i)
