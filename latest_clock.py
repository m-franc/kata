
#https://www.codewars.com/kata/58925dcb71f43f30cd00005f/train/python

def latest_clock(a, b, c, d):
    datas = [a, b, c, d]
    get_big_hour = []
    clock = []
    for data in datas:
        if data >= 0 and data < 3:
            get_big_hour.append(data)
    clock.append(max(get_big_hour))
    datas.remove(max(get_big_hour))
    get_little_hour = []
    for data in datas:
        if clock[0] == 2:
            print("ICI")
            if data >= 0 and data < 4:
                get_little_hour.append(data)
        else:
            if data >= 0 and data < 10:
                get_little_hour.append(data)
    clock.append(max(get_little_hour))
    datas.remove(max(get_little_hour))
    get_big_minute = []
    for data in datas:
        if data >= 0 and data < 6:
            get_big_minute.append(data)
    clock.append(max(get_big_minute))
    datas.remove(max(get_big_minute))
    clock.append(datas[0])
    clock = list(map(str, clock))
    return clock[0]+clock[1]+":"+clock[2]+clock[3]
    
print(latest_clock(1, 2, 8, 9))