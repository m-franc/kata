#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

import re

def solution(s):
    words = re.split(r"([A-Z])", s)
    print(words)
    join_words = " ".join(words)
    print(join_words)
    for i, c in enumerate(join_words, 1):
        if c.isupper():
            join_words = join_words.replace(join_words[i + 1], "")
    return join_words
    #new_s = ""
    #for c in s:
    #    if c.isupper():
    #        new_s += " "
    #    new_s += c
    #return new_s

print(solution("bonjourHelloKonbawa"))