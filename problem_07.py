"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7

Solution by Sam Sanft
"""
import math
import time


def generate_prime(n):
    """
    Returns the nth prime.
    """
    primes = [2]
    x = 3
    while len(primes) < n:
        root = math.sqrt(x)
        is_prime = True
        for p in primes:
            if p > root:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
        x += 2
    return primes[-1]


def problem_7():
    x = generate_prime(10_001)
    print(x)


if __name__ == "__main__":
    start_time = time.time()
    problem_7()
    print(f"Time: {time.time() - start_time}s")
