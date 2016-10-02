#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nsq

TOPIC = "t"
NSQ_HOST = "127.0.0.1"
NSQ_PORT = 4150
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def handler(msg):
    pass

def test():
    reader = nsq.Reader(topic=TOPIC, nsqd_tcp_addresses=["%s:%d" % (NSQ_HOST, NSQ_PORT)],
                        channel="c",
                        message_handler=handler)
    nsq.run()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)


