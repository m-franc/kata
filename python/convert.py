def convert(number):
    int_number = [int(i) for i in number]
    int_numbers = []
    i = 0
    while i < len(int_number) - 1:
        int_numbers.append(str(int_number[i]) + str(int_number[i + 1]))
        i += 2
    return "".join([chr(int(two_digit)) for two_digit in int_numbers])
print(convert("73327673756932858080698267658369"))