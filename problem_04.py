"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4

Solution by Sam Sanft
"""


def is_palindrome(x):
    digits = []
    i = 0
    while x / (10 ** i) > 1:
        digits.append(int(x / (10 ** i) % 10))
        i += 1
    for i in range(int(len(digits) / 2)):
        if digits[i] != digits [-(i + 1)]:
            return False
    return True


def problem_4():
    palindromes = []
    for i in range(1000):
        for j in range(1000):
            product = i * j
            if is_palindrome(product):
                palindromes.append(product)
    print(max(palindromes))


if __name__ == "__main__":
    problem_4()
