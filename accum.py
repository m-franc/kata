def accum(s):
    sentence = ""
    i = 1
    for char in s:
        o = 0
        while o < i:
            if o == 0:
                sentence = sentence + str(char.capitalize())
            else:
                sentence = sentence + str(char.lower())
            o += 1
        sentence = sentence + '-'
        i += 1
    return sentence[:-1]

print(accum("ZpglnRxqenU"))