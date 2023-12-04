def find_needle(haystack):
    for i, elem in enumerate(haystack):
        print(elem)
        if elem == "needle":
            return "found the needle at position " + str(i)
    return None

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))