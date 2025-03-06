def elevator_distance(array):
    distance = 0
    i = 0
    while i < len(array) - 1:
        if array[i] < array[i + 1]:
            distance += (array[i + 1] - array[i])
        else:
            distance += (array[i] - array[i + 1])
        print(distance)
        i += 1
    return distance

print(elevator_distance([7,1,7,1]))