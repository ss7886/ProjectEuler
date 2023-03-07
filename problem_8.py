"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9

Solution by Sam Sanft
"""


def problem_8():
    f = open("problem_8.txt")
    num_str = ""
    for line in f:
        num_str += line[:-1]

    factors = 13
    n = len(num_str)
    assert n == 1000
    champ = -1
    for i in range(n - factors + 1):
        product = 1
        for c in num_str[i:i+factors]:
            product *= int(c)
        if product > champ:
            champ = product
    print(champ)


if __name__ == "__main__":
    problem_8()
