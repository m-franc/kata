#https://www.codewars.com/kata/55f9064161541a9e01000001/train/python
import re

def valid_number(n):
    n_part = n.split(".")
    print(n_part)
    if (n_part[0] == "" or re.match("^-?[0-9]", n_part[0])) and re.match("[+-0-9]{2}", n_part[1]):
        return True
    else:
        return False

print(valid_number("34443.33"))