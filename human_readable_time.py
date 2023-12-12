#https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    hh = 0
    mm = 0
    ss = 0

    for i in range(seconds + 1):
        if i % 60 == 0:
            mm += 1
        if mm % 60 == 0:
            hh += 1
    print(f"h : {hh}, m : {mm}, s : {ss}")
    return 0

print(make_readable(67))