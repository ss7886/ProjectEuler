"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21

Solution by Sam Sanft
"""
import math


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


def function_d(primes, x):
    prime_factors = get_prime_factorization(primes, x)
    all_factors = [1]
    for prime, exp in prime_factors.items():
        new_factors = []
        for i in range(exp):
            new_factors += [f * prime ** (i + 1) for f in all_factors]
        all_factors += new_factors
    return sum(all_factors) - x


def problem_21():
    max_val = 10_000
    primes = generate_primes(max_val)
    d_vals = {}
    amicable = {}
    for i in range(max_val):
        d_vals.update({i + 1: function_d(primes, i + 1)})
    for a, b in d_vals.items():
        if b <= max_val:
            if d_vals.get(b) == a and a != b:
                amicable.update({a: b})
    print(sum(amicable.keys()))



if __name__ == "__main__":
    problem_21()
