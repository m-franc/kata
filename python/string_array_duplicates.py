#https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
def dup(array):
    new_array = []
    for elem in array:
        str = ""
        for i, c in enumerate(elem):
            if i == 0:
                str += c
            elif c != elem[i - 1]:
                str += c
        new_array.append(str)
    return new_array

print(dup(["abracadabra","allottee","assessee"]))