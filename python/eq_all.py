#https://www.codewars.com/kata/59dce15af703c42af6000035/train/python

from itertools import groupby, islice

def eq_all(iterable):
    iterator = iter(iterable)
    first = next(iterator, False)
    return all(first == elem for elem in iterator)
print(eq_all("aaaaabbbbb"))
print(next(islice(groupby(""), 1, None), False))
#print(len({}))
#print(False == True)