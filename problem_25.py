"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

https://projecteuler.net/problem=25

Solution by Sam Sanft
"""
import math
import time


def num_digits(x):
    """
    Return the number of digits in int x.
    """
    return int(math.log10(x)) + 1


def problem_25():
    a = 1
    b = 1
    i = 2
    max_len = 1_000
    while num_digits(b) < max_len:
        b = a + b
        a = b - a
        i += 1
    print(i)


if __name__ == "__main__":
    start_time = time.time()
    problem_25()
    print(f"Time: {time.time() - start_time}s")
