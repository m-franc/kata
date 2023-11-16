def capitalize(s):

    first_str = ""
    second_str = ""
    for i in range(len(s)):
        if i % 2 == 0:
            first_str += s[i].upper()
        else:
            first_str += s[i]

    for i in range(len(s)):
        if i % 2 != 0:
            second_str += s[i].upper()
        else:
            second_str += s[i]
    return [first_str, second_str]

print(capitalize("abcdef"))