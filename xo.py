def xo(s):
    x = 0
    o = 0
    for char in s:
        if char == 'x' or char == 'X':
            x += 1
        elif char == 'o' or char == 'O':
            o += 1
    if x != o:
        return False
    else:
        return True
    
print(xo("ooxx"))