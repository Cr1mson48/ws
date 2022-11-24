
from time import sleep
from pybit import usdt_perpetual

import logging
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

ws_linear = usdt_perpetual.WebSocket(
    test=True,
    api_key="JOd5rOOlZV7TaZKrNS",
    api_secret="k4tIGbeDNk3LbgkZfD8oDG55wZxVe9he6z3R"
)

def order_msg(message):
    print(message)

ws_linear.order_stream(order_msg)

while True:
    sleep(1)