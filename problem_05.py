"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5

Solution by Sam Sanft
"""
import time


def get_factorization(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    factors = {}
    remaining = x
    for p in primes:
        exp = 0
        while remaining % p == 0:
            exp += 1
            remaining /= p
        if exp > 0:
            factors[p] = exp
        if remaining == 1:
            break
    return factors


def problem_5():
    max_factor = 20
    all_factors = {}
    for i in range(2, max_factor + 1):
        factors_i = get_factorization(i)
        for prime, exp in factors_i.items():
            if prime not in all_factors:
                all_factors[prime] = exp
            if exp > all_factors[prime]:
                all_factors[prime] = exp

    factors = 1
    for prime, exp in all_factors.items():
        factors *= prime ** exp

    print(factors)


if __name__ == "__main__":
    start_time = time.time()
    problem_5()
    print(f"Time: {time.time() - start_time}s")
