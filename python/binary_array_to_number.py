def binary_array_to_number(arr):

    str_num = ""
    for num in arr:
        str_num = str_num + str(num)
    number = int(str_num, 2)

binary_array_to_number([1, 0, 1, 1])