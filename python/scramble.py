#https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
from collections import Counter

def scramble(s1, s2):
    s2 = Counter(s2)
    for c in s1:
        s2[c] -= 1
    return all(cnt <= 0 for cnt in s2.values())


print(scramble('scriptjava', 'javascript'))