def spin_around(lst):
    right = 0
    left = 0
    for dir in lst:
        if dir == "right":
            right += 1
        else:
            left += 1
    spin_r = 0
    spin_l = 0
    for r in range(right):
        if r != 0 and r % 4 == 0:
            spin_r += 1
    for l in range(left):
        if l != 0 and l % 4 == 0:
            spin_l += 1
    total_spin = spin_r - spin_l
    if total_spin < 0:
        return total_spin * -1
    else:
        return total_spin

print(spin_around(['right']))
