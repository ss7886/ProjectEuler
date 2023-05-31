"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 =
9474

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

https://projecteuler.net/problem=30

Solution by Sam Sanft
"""
import time


def problem_30():
    sums = []
    for i in range(10, 6 * 9 ** 5):
        string = str(i)
        digits_power = [int(string[j]) ** 5 for j in range(len(string))]
        if sum(digits_power) == i:
            sums.append(i)

    print(sum(sums))


if __name__ == "__main__":
    start_time = time.time()
    problem_30()
    print(f"Time: {time.time() - start_time}s")
