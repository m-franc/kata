def is_leap_year(year):
    bool = False
    if year % 100 == 0:
        bool = False
        if year % 4 == 0 and year % 400 == 0:
            bool = True
    elif year % 4 == 0 or year % 400 == 0:
        bool = True
    return bool
print(is_leap_year(2100))