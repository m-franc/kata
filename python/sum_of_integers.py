import re

def sum_of_integers_in_string(s):
    words = re.split(r"\D", s)
    numerics = list(filter(lambda word: word.isnumeric(), words))
    integers = list(map(lambda numeric: int(numeric), numerics))
    return sum(integers)
    

print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy"))