def name_in_str(string : str, name : str) -> bool:
    name = name.lower()
    string = string.lower()
 
    is_n_in_str = ""
    i = 0
    tmp_i = 0
    for cn in name:
        i = tmp_i
        while i < len(string):
            if string[i] == cn:
                is_n_in_str += cn
                i += 1
                tmp_i = i
                break
            i += 1
    print(is_n_in_str)
    if is_n_in_str == name:
        return True
    return False


print(name_in_str("thomas","Thomas"))
