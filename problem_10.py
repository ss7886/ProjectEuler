"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10

Solution by Sam Sanft
"""
import math


def problem_10():
    primes = [2]
    max_val = 2_000_000
    sum_primes = 2
    x = 3

    while x < max_val:
        root = int(math.sqrt(x))
        is_prime = True
        for p in primes:
            if p > root:
                break
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
            sum_primes += x
        x += 2

    print(sum_primes)


if __name__ == "__main__":
    problem_10()
