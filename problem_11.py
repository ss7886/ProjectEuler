"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

(See problem_11.txt)

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in
the 20×20 grid?

https://projecteuler.net/problem=11

Solution by Sam Sanft
"""


def problem_11():
    grid = []
    f = open("problem_11.txt")
    for line in f:
        row = line.split()
        for i in range(len(row)):
            row[i] = int(row[i])
        grid.append(row)

    n = 4
    champ = 0

    # horizontal
    for row in grid:
        for i in range(len(row) - n):
            product = 1
            for offset in range(n):
                product *= row[i + offset]
            if product > champ:
                champ = product

    # vertical
    for i in range(len(grid) - n):
        for j in range(len(grid[i])):
            product = 1
            for offset in range(n):
                product *= grid[i + offset][j]
            if product > champ:
                champ = product

    # top left to bottom right
    for i in range(len(grid) - n):
        for j in range(len(grid[i]) - n):
            product = 1
            for offset in range(n):
                product *= grid[i + offset][j + offset]
            if product > champ:
                champ = product

    # top right to bottom left
    for i in range(n, len(grid) - n):
        for j in range(len(grid[i]) - n):
            product = 1
            for offset in range(n):
                product *= grid[i - offset][j + offset]
            if product > champ:
                champ = product

    print(champ)


if __name__ == "__main__":
    problem_11()
