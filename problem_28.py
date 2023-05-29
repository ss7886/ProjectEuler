"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

https://projecteuler.net/problem=28

Solution by Sam Sanft
"""
import math
import time


def intuitive(n):
    """
    Calculates the answer by adding each value along the diagonal individually. Runs in linear time.
    """
    sum_val = 1
    diag_val = 1
    diag_diff = 2

    for i in range(int(n / 2)):
        for j in range(4):
            diag_val += diag_diff
            sum_val += diag_val
        diag_diff += 2
    return sum_val


def derivation(n):
    """
    Returns the answer as a single polynomial expression (2/3 n^3 + 1/2 n^2 + 4/3 n - 3/2). Runs in constant time.
    Upon inspecting the problem, one notices the diagonals can be represented by a quadratic expression in terms of n
    (for example the top right diagonal is n^2, the top left n^2 - n + 1, etc). Since the sum of the diagonals can be
    represented as the sum of multiple quadratic series, then one can infer that it will be some cubic polynomial.
    Knowing this, the correct expression can be derived using any four points, for example f(1) = 1, f(3) = 25, f(5) =
    101, f(7) = 261.

    Note: Inaccurate for very large n (n > ~1,000,000) due to imprecision in float division.
    """
    return round(2 / 3 * n ** 3 + 1 / 2 * n ** 2 + 4 / 3 * n - 1.5)


def problem_28():
    """
    Two different means of calculating the answer are provided. One is a more intuitive implementation that runs in
    linear time. The second relies on a mathematical derivation not provided in the code but runs in constant time.
    """
    n = 1001

    # print(intuitive(n))
    print(derivation(n))


if __name__ == "__main__":
    start_time = time.time()
    problem_28()
    print(f"Time: {time.time() - start_time}s")
