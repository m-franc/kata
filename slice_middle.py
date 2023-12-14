#https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python

import math

def reverse_middle(lst):
    len_lst = len(lst)
    
    if len_lst == 1:
        return lst
    elif len_lst < 4:
        return []
    len_rev_mid_lst = 2 if len_lst % 2 == 0 else 3
    half_len_lst = math.ceil(len_lst / 2)
    padding_left = half_len_lst - len_rev_mid_lst + 1
    rev_mid_lst = []
    lst.reverse()
    for i in range(padding_left, padding_left + len_rev_mid_lst):
        rev_mid_lst.append(lst[i])
    return rev_mid_lst
print(reverse_middle([43, 1, False, 'string', {}]))