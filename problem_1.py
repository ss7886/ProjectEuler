def problem_1():
    count = 0
    max_val = 1000
    a, b = 3, 5
    for i in range(a, max_val, a):
        count += i
    for i in range(b, max_val, b):
        count += i
    for i in range(a * b, max_val, a * b):
        count -= i
    print(count)

if __name__ == "__main__":
    problem_1()
