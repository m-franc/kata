def solve(strings):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph_dict = dict.fromkeys(alph, 0)
    i = 1
    for char in alph:
        alph_dict[char] += 1 * i
        i += 1
    #print(alph_dict)
    match_number = []
    for o, string in enumerate(strings):
        match_number.append(0)
        for u, char in enumerate(string):
            for letter in alph_dict.items():
                if (letter[0] == char or letter[0].upper() == char) and letter[1] == u + 1:
                    match_number[o] += 1
    return match_number

print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]))