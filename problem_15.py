"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

https://projecteuler.net/problem=15

Solution by Sam Sanft
"""


def problem_15():
    """
    For an nxn grid, the number of routes is equal to the largest value on the (2n)-th row of Pascal's triangle, or (2n
    choose n).
    """
    max_val = 20
    val = 1

    i = 1
    j = 2 * max_val

    while i < j:
        val = int(val * j / i)
        i += 1
        j -= 1

    print(val)


if __name__ == "__main__":
    problem_15()
