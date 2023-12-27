def balance(left, right):
    wht_values = {"!" : 2, "?" : 3}
    wht_r, wht_l = 0
    for l in left:
        wht_l += wht_values[l]
    for r in right:
        wht_r += wht_values[r]
    if wht_l == wht_r:
        return "Balance"
    elif wht_l > wht_r:
        return "Left"
    else:
        return "Right"
