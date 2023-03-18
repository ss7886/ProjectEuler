"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14

Solution by Sam Sanft
"""


def problem_14():
    max_val = 1_000_000
    counts = {}

    for i in range(1, max_val + 1):
        if i in counts:
            continue
        x = i
        count = 1
        chain = [x]
        while x != 1:
            if x in counts:
                count += counts[x] - 1
                break

            count += 1
            if x % 2 == 0:
                x = int(x / 2)
            else:
                x = 3 * x + 1
            chain.append(x)

        for j in range(len(chain)):
            counts[chain[j]] = count - j

    champ = 1

    for i in range(1, max_val + 1):
        if counts[i] > counts[champ]:
            champ = i

    print(f"{champ}: {counts[champ]}")


if __name__ == "__main__":
    problem_14()
