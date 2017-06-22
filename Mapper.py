#!/usr/bin/env python

import sys

from KafkaProducer import *


def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()


def main(localproducer):
    # input comes from STDIN (standard input)

    data = read_input(sys.stdin)
#Replace topictest with your topic
    localproducer.send("topictest", data.__str__())

if __name__ == "__main__":
    localproducer = KafkaProducer()
    main(localproducer)
