def distinct_digit_year(year):
    year_after = year + 1
    while len(set(str(year_after))) != len(str(year_after)):
        year_after += 1
    return year_after

print(distinct_digit_year(1987))