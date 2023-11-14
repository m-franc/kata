def get_count(sentence):
    count = 0
    for char in sentence:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count = count + 1
    return count

print(get_count("bonjour comment ca va ? oui et toi ?"))