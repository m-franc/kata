#https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python

from collections import Counter



def solve(arr):
    arr_cnt = Counter(arr).most_common()
    print(arr_cnt)
    new_arr = []
    arr_cnt = sorted(arr_cnt, key= lambda i: i[0])
    print(arr_cnt)
    for elem in arr_cnt:
        for i in range(elem[1]):
            new_arr.append(elem[0])
    return new_arr

print(solve([5,9,6,9,6,5,9,9,4,4]))