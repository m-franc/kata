#https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

def arrange(s):
    t = []
    while s != []:
        t.append(s[0])
        t.append(s[-1])
        s.reverse()
        s.pop(0)
        if s != []:
            s.pop(-1)
    return t

print(arrange([1,2,3,4,5,6]))