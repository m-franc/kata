def highest_rank(arr):
    arr_no_freq = dict.fromkeys(arr, 0)
    if len(arr_no_freq) == len(arr):
        return max(arr)
    for elem_no_freq in arr_no_freq.items():
        for elem in arr:
            if elem == elem_no_freq[0]:
                arr_no_freq[elem] += 1
    highest_rank = 0
    nb_freq_max = 0
    for elem in arr_no_freq.items():
        if nb_freq_max < elem[1] or (nb_freq_max == elem[1] and elem[0] > highest_rank):
            nb_freq_max = elem[1]
            highest_rank = elem[0]
    return highest_rank
print(highest_rank([1, 1, 2, 2, 3]))