def is_isogram(string):

    lst = list(dict.fromkeys((string.lower())))
    if len(string) == len(lst):
        return True
    else:
        return False

print(is_isogram("moOse"))