def quicksum(packet):
    if not all((c.isalpha() and c.isupper()) or c.isspace() for c in packet):
        return 0
    result = 0
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph_dict = dict.fromkeys(alph, 0)
    i = 1
    for letter in alph:
        alph_dict[letter] += 1 * i
        i += 1
    for i, elem in enumerate(packet, 1):
        if elem == ' ':
            continue
        else:
            result += i * alph_dict[elem]
    return result

print(quicksum("As"))