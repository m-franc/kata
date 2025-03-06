def format_money(amount):
    p_amount = format(amount, ".2f")
    str_format = "$" + str(p_amount)
    return str_format
print(format_money(3.1))