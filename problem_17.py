"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

https://projecteuler.net/problem=17

Solution by Sam Sanft
"""
import time


def num_letters(x):
    """
    Returns the number of letters of an integer x in string form.
    """
    letters = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7,
               16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
    num = 0
    last_two = x
    if x == 1000:
        return 11  # "one thousand"
    if 100 <= x < 1000:
        first_digit = int(x / 100)
        num += letters[first_digit]
        num += 7  # "hundred"
        last_two -= first_digit * 100
        if last_two != 0:
            num += 3  # "and"
    if last_two < 20:
        num += letters[last_two]
    else:
        tens = int(last_two / 10) * 10
        ones = last_two % 10
        num += letters[tens] + letters[ones]
    return num


def problem_17():
    max_val = 1000
    val = 0
    for i in range(max_val):
        val += num_letters(i + 1)
    print(num_letters(342))
    print(num_letters(115))
    print(val)


if __name__ == "__main__":
    start_time = time.time()
    problem_17()
    print(f"Time: {time.time() - start_time}s")
