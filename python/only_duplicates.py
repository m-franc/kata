#https://www.codewars.com/kata/5a1dc4baffe75f270200006b/train/python

from collections import Counter

def only_duplicates(st):
    return "".join([c for c in st if Counter(st)[c] > 1])
print(only_duplicates("abccdefee"))

i = 4
i.append(5)