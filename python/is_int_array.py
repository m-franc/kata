#https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python

def is_int_array(arr):
    if isinstance(arr, list) == False or arr == None:
        return False
    for elem in arr:
        if isinstance(elem, float) == True:
            if elem.is_integer() == False:
                return False
        elif isinstance(elem, int) == False:
            return False
    return True


print(is_int_array({514}))