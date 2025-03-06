#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):
    if arr is None or False or len(arr) < 2 or arr == 0:
        return 0
    return sum(arr) - (min(arr) + max(arr))
print(sum_array([6, 2, 1, 8, 10]))