"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7

Solution by Sam Sanft
"""
import math


def generate_primes(num):
    primes = [2]
    x = 3
    while len(primes) < num:
        root = math.sqrt(x)
        isPrime = True
        for p in primes:
            if p > root:
                break
            if x % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)
        x += 2
    return primes[-1]


def problem_7():
    x = generate_primes(10_001)
    print(x)


if __name__ == "__main__":
    problem_7()
