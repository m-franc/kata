def pattern(n):
    if n <= 0:
        return print("send value > 0")
    i = 1
    pattern = str(1)
    while i < n:
        pattern = pattern + '\n'
        if n >= 2:
            n_star = 0
            stars = ''
            while n_star < i:
                stars = stars + '*'
                n_star = n_star + 1
            pattern = pattern + str(1) + stars
        i = i + 1
        pattern = pattern + str(i)
    return pattern

print(pattern(90))