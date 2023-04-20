"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4

Solution by Sam Sanft
"""
import time


def is_palindrome(x):
    """
    Returns whether or not x is a palindrome as a boolean.
    """
    str_x = str(x)
    mid = int(len(str_x) / 2)
    odd = len(str_x) % 2 == 1
    if odd:
        return str_x[:mid] == str_x[mid + 1:][::-1]
    else:
        return str_x[:mid] == str_x[mid:][::-1]


def problem_4():
    palindromes = []
    for i in range(1000):
        for j in range(1000):
            product = i * j
            if is_palindrome2(product):
                palindromes.append(product)
    print(max(palindromes))


if __name__ == "__main__":
    start_time = time.time()
    problem_4()
    print(f"Time: {time.time() - start_time}s")
