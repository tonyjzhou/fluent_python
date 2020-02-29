import bisect
import random
from datetime import datetime


def insort_demo(size: int):
    random.seed(datetime.now())

    order_seq = []
    for i in range(size):
        bisect.insort(order_seq, random.randrange(size))

        print("%2d ->" % i, order_seq)


if __name__ == "__main__":
    insort_demo(10)
