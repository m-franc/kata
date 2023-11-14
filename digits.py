def digits(num):

    list_num = []
    str_num = str(num)

    for digit in str_num:
        list_num.append(int(digit))
    copy_list_num = list_num
    big_list = []
    o = 0
    i = 0
    while o < len(list_num):
        i = o + 1
        while i < len(copy_list_num):
            big_list.append(list_num[o] + copy_list_num[i])
            i += 1
        o += 1
    return big_list
print(digits(12345))