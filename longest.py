def string_to_array(s):
    return [c for c in s]

def longest(a1, a2):
    all_a = a1 + a2
    sorted_all_a = sorted(all_a)
    array_all_a = string_to_array(sorted_all_a)
    dict_all_a = dict.fromkeys(array_all_a)
    str_all_a = ""
    for elem in dict_all_a:
        str_all_a += elem
    return str_all_a

print(longest("fhcudsifhdsf", "fdsshgkjfydfsghg"))