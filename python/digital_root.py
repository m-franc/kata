#https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

def digital_root(n):
    digits = []
    if n < 10:
        return n
    else:
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digital_root(sum(digits))
    
print(digital_root(493193))