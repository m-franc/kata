#https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

import re
from string import ascii_uppercase as alph_up
from string import ascii_lowercase as alph_dn

def roting(str):
    if str.group(0).isupper():
        rot13 = (alph_up.index(str.group(0)) + 13) % 26
        return alph_up[rot13]
    if str.group(0).islower():
        rot13 = (alph_dn.index(str.group(0)) + 13) % 26
        return alph_dn[rot13]

def rot13(message):
    return re.sub(r"([a-zA-Z])", roting, message)

print(rot13("bonjour"))