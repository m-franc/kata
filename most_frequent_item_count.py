def most_frequent_item_count(collection):
    if collection == []:
        return 0
    collection.sort()
    each_count = []
    for i in range(len(collection)):
        each_count.append(0)
    o = 0
    for i in range(len(collection) - 1):
        if collection[i] == collection[i + 1]:
            each_count[o] += 1
        else:
            o += 1
    max = 0
    print(each_count)
    for elem in each_count:
        if elem > max:
            max = elem
    return max + 1

print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))