def sum_two_smallest_numbers(numbers):
    numbers.sort()
    i = 0
    for number in numbers:
        first_smallest = numbers[0]
        second_smallest = numbers[1]
    return first_smallest + second_smallest

print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))