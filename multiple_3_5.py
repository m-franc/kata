#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    factors = []
    for factor in range(number):
        if factor % 3 == 0 or factor % 5 == 0:
            factors.append(factor)
    return sum(factors)

print(solution(200))