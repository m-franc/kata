def digitize(n):
    str_n = str(n)
    digits = []
    for char in str_n:
        digits.append(int(char))
    reversed_digits = list(reversed(digits))
    return reversed_digits
print(digitize(123456))