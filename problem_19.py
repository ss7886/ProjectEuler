"""
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

https://projecteuler.net/problem=19

Solution by Sam Sanft
"""


def problem_19():
    month = 1
    year = 1900
    day = 2
    count = 0
    while year < 2001:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day += 3
        if month in [4, 6, 9, 11]:
            day += 2
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day += 1
        if day > 7:
            day -= 7
        month += 1
        if month > 12:
            year += 1
            month -= 12
        if 1901 <= year <= 2000 and day == 1:
            count += 1
    print(count)


if __name__ == "__main__":
    problem_19()
