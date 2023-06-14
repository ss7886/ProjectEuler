"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

https://projecteuler.net/problem=31

Solution by Sam Sanft
"""
import time


def f(x, max_coin=7, saved=None):
    if x == 1 or x == 0:
        return 1
    if max_coin == 1:
        return int(x / 2) + 1
    if saved is None:
        saved = {}
    if (x, max_coin) in saved:
        return saved[(x, max_coin)]

    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    count = 0
    rem = x

    while x < denominations[max_coin]:
        max_coin -= 1

    while rem >= 0:
        count += f(rem, max_coin - 1, saved)
        rem -= denominations[max_coin]
    saved[(x, max_coin)] = count
    return count


def problem_31():
    print(f(200))


if __name__ == "__main__":
    start_time = time.time()
    problem_31()
    print(f"Time: {time.time() - start_time}s")
