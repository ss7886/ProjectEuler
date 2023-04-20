"""
The sum of the squares of the first ten natural numbers is: 385

The square of the sum of the first ten natural numbers is: 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is: 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6

Solution by Sam Sanft
"""
import time


def problem_6():
    cap = 100
    squared_sum = int((cap + 1) * (cap / 2))
    squared_sum *= squared_sum
    sum_squares = 0
    for i in range(1, cap + 1):
        sum_squares += i * i
    print(squared_sum - sum_squares)


if __name__ == "__main__":
    start_time = time.time()
    problem_6()
    print(f"Time: {time.time() - start_time}s")
