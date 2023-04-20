"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

Solution by Sam Sanft
"""
import math
import time


def problem_10():
    max_val = 2_000_000
    prime = [True] * (max_val - 1)
    p = 2
    sqrt_val = math.sqrt(max_val)
    while p < sqrt_val:
        i = 2 * p
        while i < max_val:
            prime[i - 1] = False
            i += p
        p += 1
        while not prime[p - 1]:
            p += 1

    sum_val = -1
    for i in range(max_val - 1):
        if prime[i]:
            sum_val += i + 1

    print(sum_val)


if __name__ == "__main__":
    start_time = time.time()
    problem_10()
    print(f"Time: {time.time() - start_time}s")
