def bubblesort_once(l):
    i = 0
    size = len(l)
    while i < size - 1:
        if l[i + 1] == None:
            break
        else:
            if l[i] > l[i + 1]:
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp
        i += 1
    return l



print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))