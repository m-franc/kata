def time_convert(num):
    hours, minutes = 0, 0
    for minute in range(num):
        minutes += 1
        if minutes == 60:
            hours += 1
            minutes = 0
    times = [hours, minutes]
    return ":".join(str(t) if t > 9 else "0" + str(t) for t in times)

print(time_convert(970))