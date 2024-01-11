
#https://www.codewars.com/kata/58925dcb71f43f30cd00005f/train/python

def latest_clock(a, b, c, d):
    datas = [a, b, c, d]
    datas.sort(reverse=True)
    print(datas)
print(latest_clock(1, 2, 8, 9))