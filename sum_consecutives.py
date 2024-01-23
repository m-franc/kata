#https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python

from collections import Counter
from itertools import groupby
def sum_consecutives(lst):
    if lst == []:
        return 0
    new_lst = []
    new_lst.append(lst[0])
    fst_ptl_ste = lst[0]
    i = 0
    for elem in lst[1:]:
        if fst_ptl_ste == elem:
            new_lst[i] += fst_ptl_ste
        else:
            new_lst.append(elem)
            fst_ptl_ste = elem
            i += 1
    return new_lst

#print(sum_consecutives([-5, -5, 7, 7, 12, 0]))
#for key, group in groupby([12, 12, 12, 12, -5, -5, 7, 7, 12, 0]):
#    print(f"nouvelle elem : {key}")
#    for elem in group:
#        print(elem)
print([sum(group) for key, group in groupby([12, 12, 12, 12, -5, -5, 7, 7, 12, 0])])
#print(Counter([12, 12, 12, 12, -5, -5, 7, 7, 12, 0]))