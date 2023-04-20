"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

https://projecteuler.net/problem=3

Solution by Sam Sanft
"""


import math
import time


def generate_primes(max_val):
    """
    Returns complete list of prime values less than or equal to max_val
    """
    primes_sqrt = [2]
    primes = [2]
    sqrt_val = math.sqrt(max_val)
    i = 3
    largest = 3
    while i <= max_val:
        prime = True
        for p in primes_sqrt:
            if i % p == 0:
                prime = False
                break
        if prime:
            if i < sqrt_val:
                primes_sqrt.append(i)
            primes.append(i)
            largest = i
        i += 2
    return primes


def problem_3():
    val = 600_851_475_143
    primes = generate_primes(math.sqrt(val))
    factors = []

    champ = -1

    for p in primes:
        if val % p == 0:
            champ = p

    print(champ)


if __name__ == "__main__":
    start_time = time.time()
    problem_3()
    print(f"Time: {time.time() - start_time}s")
