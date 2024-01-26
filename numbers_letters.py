#https://www.codewars.com/kata/599febdc3f64cd21d8000117/train/python

from collections import deque

def numbers_of_letters(n):
    letters_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    all_n_in_letters = deque()
    while (n != 4):
        digits = list(map(int, str(n)))
        n_in_letters = ""
        for digit in digits:
            n_in_letters += letters_digits[digit]
        all_n_in_letters.append(n_in_letters)
        n = len(n_in_letters)
    all_n_in_letters.append("four")
    return list(all_n_in_letters)

letters_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(numbers_of_letters(999))