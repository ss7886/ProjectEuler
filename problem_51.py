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
import math


def generate_primes(max_val):
    """
    Returns complete list of prime values less than or equal to max_val
    """
    primes_sqrt = [2]
    primes = [2]
    sqrt_val = math.sqrt(max_val)
    i = 3
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


def get_replacements(x, digits_binary):
    """
    Returns a list of the number x with specified digits replaced by values 0-9.
    """
    replace_digits = []
    for i in range(digits(x)):
        replace_digits.append(digits_binary & (2 ** i))

    values = []
    for i in range(len(replace_digits)):
        values.append(int(x % (10 ** (i + 1)) / (10 ** i)) * (10 ** i))

    assert sum(values) == x

    replacements = []
    for d in range(10):
        r = x
        for i in range(len(replace_digits)):
            if not replace_digits[i]:
                continue

            r = r - values[i] + d * (10 ** i)
        replacements.append(r)

    return replacements


def is_prime(x, primes):
    """
    Checks whether x is divisible by any value in primes.
    """
    for p in primes:
        if p >= x:
            return True
        if x % p == 0:
            return False
    return True


def problem_51():
    magic_number = 8
    p_10_000_000 = generate_primes(1_000_000)
    p_4000 = generate_primes(1000)
    print("generated primes")
    for p in p_10_000_000:
        for i in range(1, 2 ** digits(p) - 1):
            replacements = get_replacements(p, i)
            count = 0
            if p not in replacements:
                continue
            for r in replacements:
                if digits(r) < digits(p):
                    count += 1
                    continue
                if not is_prime(r, p_4000):
                    count += 1
                    if count > 10 - magic_number:
                        break
            if count <= 10 - magic_number:
                primes = []
                for r in replacements:
                    if is_prime(r, p_4000):
                        primes.append(r)
                print(p, primes)
                return


if __name__ == "__main__":
    problem_51()
