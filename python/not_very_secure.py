#https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python

import re

def alphanumeric(password):

    return True if re.match("^[A-Za-z0-9]*$", password) else False

print(alphanumeric("hgfdhgfdhfdg6758678678!GHUIKGYKGJH"))