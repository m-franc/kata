#https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python


def delete_zeros(number):
    if number == 0:
        return False
    return True

def move_zeros(lst):
    new_lst = list(filter(delete_zeros, lst))
    for i in range(lst.count(0)):
        new_lst.append(0)
    return new_lst

def move_zeros2(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool, reverse=True)



print(move_zeros2([1, 0, 1, 2, 0, 1, 3]))