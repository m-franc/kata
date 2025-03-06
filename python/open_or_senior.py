def open_or_senior(data):
    cat_mem_list = []
    for elem in data:
        if elem[0] >= 55 and elem[1] > 7:
            cat_mem_list.append("Senior")
        else:
            cat_mem_list.append("Open")
    return cat_mem_list


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))