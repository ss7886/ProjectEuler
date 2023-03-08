"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9

Solution by Sam Sanft
"""


def problem_9():
    magic_num = 1000
    a = 6
    b = a + 1
    c = a + 3

    while a + b + c < magic_num:
        while c ** 2 - b ** 2 != a ** 2:
            b += 1
            c += 1

        i = 1
        while i * (a + b + c) < magic_num:
            i += 1

        if i * (a + b + c) == magic_num:
            print(f"{i * a} * {i * b} * {i * c} = {a * b * c * (i ** 3)}")
            return
        else:
            a += 2
            b = a + 1
            c = a + 3

    print("No valid triples found")


if __name__ == "__main__":
    problem_9()
