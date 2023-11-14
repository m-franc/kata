def diamond(n):
    if n % 2 == 0:
        return False
    diamonds = n*[n*["*"]]
    y = 0
    for row in diamonds:
        x = 0
        for char in row:
            if x == n / 2:
                row[x] = ' '
            x += 1
        y += 1
    return diamonds

print(diamond(5))