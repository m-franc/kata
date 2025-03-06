#https://www.codewars.com/kata/584cfac5bd160694640000ae/train/python

def domino_reaction(s):
    falling = 1
    s_copy = ""
    for domino in s:
        if domino == '|' and falling == 1:
            s_copy += '/'
        elif domino == ' ' or domino == '/':
            falling = 0
            s_copy += domino
        else:
            s_copy += domino
    return s_copy

print(domino_reaction("||| ||||//| |/"))