"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

(See problem_18.txt)

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

https://projecteuler.net/problem=17

Solution by Sam Sanft
"""


def problem_18():
    raw_data = []
    f = open("problem_18.txt")
    for line in f:
        split = line.split()
        ints = [int(i) for i in split]
        raw_data.append(ints)
    n = len(raw_data)

    path_length = []
    for i in range(len(raw_data)):
        if i == 0:
            path_length.append([raw_data[0][0]])
            continue
        line = []
        for j in range(len(raw_data[i])):
            path = raw_data[i][j]
            if j == 0:
                path += path_length[i - 1][j]
            elif j == i:
                path += path_length[i - 1][j - 1]
            else:
                path += max(path_length[i - 1][j], path_length[i - 1][j - 1])
            line.append(path)
        path_length.append(line)

    print(max(path_length[n - 1]))


if __name__ == "__main__":
    problem_18()
