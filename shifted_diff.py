#https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python

def shifted_diff(first, second):
    print(second + second)
    o = len(first)
    while o > 0:
        if first[o:] + first[:o] == second:
            return len(first) - o
        o -= 1
    return -1

print(shifted_diff("bonjour","onjourb"))