
def find_screen_height(width, ratio): 
    array_ratio = ratio.split(":")
    num_ratio = int(array_ratio[0]) / int(array_ratio[1])
    height = width / num_ratio
    return str(width) + 'x' + str(height)[:-2]
print(find_screen_height(2160, "3:2"))