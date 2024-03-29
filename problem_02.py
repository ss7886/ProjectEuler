"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.

https://projecteuler.net/problem=2

Solution by Sam Sanft
"""
import time


def problem_2():
    max_val = 4_000_000
    a = 1
    b = 1
    count = 0
    while a + b < max_val:
        temp = b
        b = a + b
        a = temp
        if b % 2 == 0:
            count += b
    print(count)


if __name__ == "__main__":
    start_time = time.time()
    problem_2()
    print(f"Time: {time.time() - start_time}s")
