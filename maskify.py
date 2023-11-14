# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    str_len_to_hide = len(cc) - 4
    str_masked = ""
    for i in range(str_len_to_hide):
        str_masked += "#"
    for i in range(4):
        str_masked += cc[str_len_to_hide + i]
    return str_masked

print(maskify("123"))