def printer_error(s):
    len_s = len(s)
    errors = 0
    for char in s:
        if ord(char) > ord('m'):
            errors += 1
    return str(errors) + "/" + str(len_s)

print(printer_error("abcdefghijklmnopqrstuvwxyz"))