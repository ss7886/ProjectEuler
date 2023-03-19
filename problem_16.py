"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

https://projecteuler.net/problem=16

Solution by Sam Sanft
"""
import math


def get_digits(x):
    """
    Returns the digits of a value x in an array.
    """
    digits = []
    string = str(x)
    for i in range(len(string)):
        digits.append(int(string[i]))
    return digits


def problem_16():
    val = 2 ** 1000
    digits = get_digits(val)

    val = 0
    for i in digits:
        val += i
    print(val)


if __name__ == "__main__":
    problem_16()
