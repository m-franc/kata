#https://www.codewars.com/kata/56459c0df289d97bd7000083
def generator (From, To, Step):
    sequence = []
    if Step == 0:
        return sequence
    from_cpy = From
    if from_cpy < To:
        while from_cpy <= To:
            sequence.append(from_cpy)
            from_cpy += Step
    else:
        while from_cpy >= To:
            sequence.append(from_cpy)
            from_cpy -= Step
    return sequence

print(generator(10, 20, 0))