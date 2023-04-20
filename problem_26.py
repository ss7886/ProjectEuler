"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

https://projecteuler.net/problem=26

Solution by Sam Sanft
"""
import math
import time


def cycle(x):
    """
    Returns the recurring cycle for the reciprocal of x (ie cycle(7) returns '152857').
    """
    dividend = 1
    digit = 0
    remainders = {dividend: digit}
    quotient = []
    while True:
        i = 1
        while dividend < x:
            dividend *= 10
            if i > 1:
                quotient.append(0)
            i += 1
            digit += 1
        quotient.append(int(dividend / x))
        remainder = dividend % x

        if remainder in remainders:
            return quotient[remainders[remainder]:]
        elif remainder == 0:
            return ""
        else:
            remainders.update({remainder: digit})
            dividend = remainder
            digit += 1


def problem_26():
    champ = 0
    champ_len = 0
    max_val = 1_000
    for i in range(1, max_val + 1):
        if len(cycle(i)) > champ_len:
            champ_len = len(cycle(i))
            champ = i
    print(champ)


if __name__ == "__main__":
    start_time = time.time()
    problem_26()
    print(f"Time: {time.time() - start_time}s")
