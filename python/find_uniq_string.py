#https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/train/python

from collections import Counter
from operator import itemgetter
import re

def find_uniq(arr):
    reduced_string = [e.lower() for e in arr]
    reduced_string = list(map(set, reduced_string))
    reduced_string = list(map(str, reduced_string))
    onlyonechar = []
    for elem in reduced_string:
        onechar = re.search(r"[\{\}\']", elem)
        onlyonechar.append(onechar)
    
    print(onlyonechar)
    value = reduced_string[0]
    idx = 0
    while value != reduced_string[idx]:
        idx += 1
    return arr[idx]
print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))