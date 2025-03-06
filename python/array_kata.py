def array_diff(a, b):
    if b == []:
        return a
    for a_elem in a:
        for b_elem in b:
            if a_elem == b_elem:
                a.remove(a_elem)
    return a
print(array_diff([1,2,3], [1, 2]))