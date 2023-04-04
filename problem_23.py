"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

https://projecteuler.net/problem=23

Solution by Sam Sanft
"""
import math
import time


def generate_primes(n, primes=None):
    """
    Generates primes (starting from a list of known primes) up to value n.
    """
    if primes is None:
        primes = [2]

    x = primes[-1] + 2
    if x % 2 == 0:
        x -= 1

    while x < n:
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
    return primes


def get_prime_factorization(primes, x):
    """
    Returns the prime factorization for a natural number x
    """
    factors = {}
    for p in primes:
        count = {p: 0}
        while x % p == 0:
            x /= p
            count[p] += 1
        if count[p] > 0:
            factors.update(count)
        if x == 1:
            break

    return factors


def sum_factors(primes, x):
    prime_factors = get_prime_factorization(primes, x)
    all_factors = [1]
    for prime, exp in prime_factors.items():
        new_factors = []
        for i in range(exp):
            new_factors += [f * prime ** (i + 1) for f in all_factors]
        all_factors += new_factors
    return sum(all_factors) - x


def bsearch(list_ints, x):
    """Returns True if x is contained in a sorted list of numerical values list_ints."""
    lo = 0
    hi = len(list_ints) - 1

    while lo < hi:
        mid = int(lo + (hi - lo) / 2)
        val = list_ints[mid]
        if val == x:
            return True
        elif val < x:
            lo = mid + 1
        else:
            hi = mid

    return list_ints[lo] == x


def sum_abundant(abundant, x):
    """Returns True if x can be expressed as the sum of two abundant numbers."""
    for j in abundant:
        if j > x / 2:
            return False
        if bsearch(abundant, x - j):
            return True


def problem_23():
    max_val = 28123
    primes = generate_primes(max_val)

    abundant = []
    for i in range(1, max_val):
        if sum_factors(primes, i) > i:
            abundant.append(i)

    count = 0
    for i in range(1, max_val + 1):
        if not sum_abundant(abundant, i):
            count += i

    print(count)


if __name__ == "__main__":
    start_time = time.time()
    problem_23()
    print(f"Time: {time.time() - start_time}s")
