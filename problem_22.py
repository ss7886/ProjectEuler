"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

https://projecteuler.net/problem=22

Solution by Sam Sanft
"""


def problem_22():
    f = open("problem_22_names.txt")
    names = f.readline().split(",")
    names = [s[1:-1] for s in names]
    names.sort()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphascores = {}
    for i in range(len(alphabet)):
        alphascores[alphabet[i]] = i + 1

    score = 0
    for i in range(len(names)):
        name_score = 0
        for j in range(len(names[i])):
            name_score += alphascores[names[i][j]]
        score += name_score * (i + 1)

    print(score)




if __name__ == "__main__":
    problem_22()
