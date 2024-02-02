#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

from collections import Counter

def first_non_repeating_letter(s):
    s_lw = s.lower()
    count_s = Counter(s_lw)
    print(count_s)
    for i, c in enumerate(s_lw):
        if count_s[c] == 1:
            return s[i]
    return ""

print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))