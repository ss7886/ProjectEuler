"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20

Solution by Sam Sanft
"""
import math
import time


def sum_digits(x):
    """
    Returns the sum of the digits of a positive integer x.
    """
    str_x = str(x)
    count = 0
    for i in range(len(str_x)):
        count += int(str_x[i])
    return count


def problem_20():
    max_factor = 100
    factorial = 1
    for i in range(max_factor):
        factorial *= (i + 1)
    print(sum_digits(factorial))


if __name__ == "__main__":
    start_time = time.time()
    problem_20()
    print(f"Time: {time.time() - start_time}s")
