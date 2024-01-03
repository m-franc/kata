#https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python

import re

def remove(st):
    sts = st.split()
    rev_sts = list(map(lambda x: x[::-1], sts))
    new_sts = []
    for st in rev_sts:
        if st[0] == '!':
            i = 0
            while st[i] == '!':
                i += 1
            new_sts.append(st[i:])
        else:
            new_sts.append(st)
    new_sts = list(map(lambda x: x[::-1], new_sts))
    return "".join(new_sts)

print(remove("!!!Hi !!hi!!! !hi"))