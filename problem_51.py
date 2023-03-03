"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53,
73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

https://projecteuler.net/problem=51

Solution by Sam Sanft
"""


def generate_primes(max_val):
    """
    Returns complete list of prime values less than or equal to max_val
    """
    primes = [2]
    i = 3
    while i <= max_val:
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        i += 2
    return primes


def digits(x):
    """
    Returns the number of digits of x.
    """
    i = 1
    while x / (10 ** i) >= 1:
        i += 1

    return i


def problem_51():
    p_100_000 = generate_primes(100_000)
    for p in p_100_000:
        pass


if __name__ == "__main__":
    problem_51()