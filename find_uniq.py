#https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

from collections import Counter

def find_uniq(arr):
    a, b = set(arr)
    print(a)
    print(b)
    group_arr = Counter(arr)
    print(group_arr)
    n = 0
    for elem in group_arr.items():
        if elem[1] == 1:
            return elem[0]

print(find_uniq([ 3, 10, 3, 3, 3 ]))