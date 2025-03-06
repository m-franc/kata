def build_string(*args):
    sentence = "I like "
    for arg in args:
        sentence = sentence + arg + ", "
    chars_sentence = list(sentence)
    chars_sentence.pop(len(sentence) - 1)
    chars_sentence.pop(len(sentence) - 2)
    chars_sentence.append('!')
    return ''.join(chars_sentence)
print (build_string("chocolate", "oat", "peanuts"))