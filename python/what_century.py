#https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

def what_century(year):
    if year[len(year) - 2:] == "00":
        ctry_nb = int(year[:len(year) - 2])
    else:
        ctry_nb = int(year[:len(year) - 2]) + 1

    ctry_nb = str(ctry_nb)
    periods = ["st", "nd", "rd", "th"]
    century = ctry_nb + periods[3]
    match ctry_nb:
        case "21" | "31" | "41" | "51" | "61" | "71" | "81" | "91":
            century = ctry_nb + periods[0]
        case "22" | "32" | "42" | "52" | "62" | "72" | "82" | "92":
            century = ctry_nb + periods[1]
        case "23" | "33" | "43" | "53" | "63" | "73" | "83" | "93":
            century = ctry_nb + periods[2]
    return century

print(what_century("7007"))