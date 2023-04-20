"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

(See problem_8.txt)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
product?

https://projecteuler.net/problem=8

Solution by Sam Sanft
"""
import time


def problem_8():
    f = open("problem_08.txt")
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
    start_time = time.time()
    problem_8()
    print(f"Time: {time.time() - start_time}s")
