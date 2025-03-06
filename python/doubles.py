def is_allthesame(s):
    if len(s) == 1:
        return False
    print(s)
    fchar = s[0]
    for char in s:
        if char != fchar:
            return False
    return True


def doubles(s):
    str = ""
    i = 0
    len_s = len(s)
    while i < len_s:
        if is_allthesame(s[i:i + 2]) == False:
            str += s[i]
        else:
            i += 1
        i += 1
    return str

print(doubles("vvvvvoiiiiin"))
s = "bonjour"
print(s*2)