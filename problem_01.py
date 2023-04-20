"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1

Solution by Sam Sanft
"""
import time


def problem_1():
    count = 0
    max_val = 1000
    a, b = 3, 5
    for i in range(a, max_val, a):
        count += i
    for i in range(b, max_val, b):
        count += i
    for i in range(a * b, max_val, a * b):
        count -= i
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    problem_1()
    print(f"Time: {time.time() - start_time}s")
