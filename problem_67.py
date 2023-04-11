"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

(see problem_67_triangle.txt)

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it. ;o)

https://projecteuler.net/problem=67

Solution by Sam Sanft
"""
import time


def problem_67():
    raw_data = []
    f = open("problem_67_triangle.txt")
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
    start_time = time.time()
    problem_67()
    print(f"Time: {time.time() - start_time}s")
