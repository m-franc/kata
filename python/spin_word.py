# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split(" "))

# very best alternative there : https://www.codewars.com/kata/reviews/55401901b8a14241e4000048/groups/56101e814d4ddcae7e000034