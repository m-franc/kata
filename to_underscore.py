#https://www.codewars.com/kata/529b418d533b76924600085d/train/python

def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    words = []
    idx_new_wd = 0
    for i, c in enumerate(string):
        if c.isupper() and i != 0:
            words.append(string[idx_new_wd:i])
            idx_new_wd = i
    words.append(string[idx_new_wd:len(string)])
    words = list(map(lambda w: w.lower(), words))
    return "_".join(words)

print(to_underscore("JustATest"))