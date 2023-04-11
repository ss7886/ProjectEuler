"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

https://projecteuler.net/problem=24

Solution by Sam Sanft
"""
import math
import time


def permutations(string, n, factorial=None):
    """
    Returns the nth lexicographic permutation of characters in string.
    """
    if len(string) == 1:
        return string[0]

    if factorial is None:
        product = 1
        for i in range(len(string) - 1):
            product *= (i + 1)
        factorial = product

    if n == 0:
        n += len(string) * factorial

    str_sorted = sorted(string)
    i = math.ceil(n / factorial)
    rem = n % factorial
    res = str_sorted[i - 1]
    str_new = str_sorted[:i - 1] + str_sorted[i:]
    return res + permutations(str_new, rem, factorial / (len(string) - 1))


def problem_24():
    digits = "0123456789"
    n = 1_000_000

    print(permutations(digits, n))


if __name__ == "__main__":
    start_time = time.time()
    problem_24()
    print(f"Time: {time.time() - start_time}s")
