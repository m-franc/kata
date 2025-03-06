def contain_all_rots(string, arr):
    rots_number = 0
    s_len = string
    rotations = []
    for i in range(s_len):
        rotations.append(string[-i:] + string[:-i])

    for elem in arr:
        for rotation in rotations:
            if elem == rotation:
                rots_number += 1
    if rots_number == s_len:
        return True
    else:
        return False
contain_all_rots("salut")