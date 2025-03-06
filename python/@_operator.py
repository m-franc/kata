def a_operation(a, b):
    if b == 0:
        return None
    return (a + b) + (a - b) + (a * b) + (a // b)

def evaluate(equation):
    numbers = equation.split(' ')
    for i, number in enumerate(numbers):
        if number == '@':
            numbers.pop(i)
    numbers = [int(number) for number in numbers]
    result = 0
    i = 0
    result = numbers[0]
    while i < len(numbers) - 1:
        result = a_operation(result, numbers[i + 1])
        if result == None:
            return None
        i += 1
    return result

print(evaluate("1 @ 1 @ -4"))