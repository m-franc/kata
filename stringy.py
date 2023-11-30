def stringy(size):
    i = 0
    str = ""
    while i < size:
        if i % 2 == 0:
            str += "1"
        else:
            str += "0"
        i += 1
    return str

print(stringy(9))