"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n =
40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <=
79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.

https://projecteuler.net/problem=27

Solution by Sam Sanft
"""
import math
import time


def consecutive(a, b, primes):
    """
    Returns for how many consecutive values of n, the formula n^2 + an + b returns a prime number, starting with n = 0.
    """
    n = 0
    while n ** 2 + a * n + b in primes:
        n += 1
    return n


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


def problem_27():
    primes_1000 = generate_primes(1000)
    searchable_primes = set(generate_primes(5_000_000, primes=primes_1000.copy()))
    primes_1000 += [1]

    champ = 0
    champ_vals = -1, -1

    for a in range(-999, 1000):
        for b in primes_1000:
            current = consecutive(a, b, searchable_primes)
            if current > champ:
                champ = current
                champ_vals = a, b

    print(f"{champ_vals[0]} x {champ_vals[1]} = {champ_vals[0] * champ_vals[1]}, 0 <= n <= {champ}")


if __name__ == "__main__":
    start_time = time.time()
    problem_27()
    print(f"Time: {time.time() - start_time}s")
