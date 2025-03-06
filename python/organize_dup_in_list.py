#https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python

from collections import Counter

def group(arr):
    arr_dcnt = Counter(arr)
    for x in arr_dcnt.elements():
        print(x)
    arr_dup = []
    for elem in arr_dcnt.items():
        dup = []
        for i in range(elem[1]):
            dup.append(elem[0])
        arr_dup.append(dup)
    return arr_dup

print(group([3, 2, 6, 2, 1, 3]))