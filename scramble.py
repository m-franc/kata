#https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

def scramble(s1, s2):
    for c in s2:
        if c in s1:
            s1 = s1.replace(c, "", 1)
        else:
            return False
    return True


print(scramble('scriptjava', 'javascript'))