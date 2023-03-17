"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(See problem_13.txt)

https://projecteuler.net/problem=13

Solution by Sam Sanft
"""


def problem_13():
    f = open("problem_13.txt")
    first_11 = []
    for line in f:
        first_11.append(int(line[0:11]))

    print(str(sum(first_11))[0:10])


if __name__ == "__main__":
    problem_13()
