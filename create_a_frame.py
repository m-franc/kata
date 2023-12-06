#https://www.codewars.com/kata/5672f4e3404d0609ec00000a/train/python


def fill_word(word, elem):
    #print(f"le fruit : {word} et la ligne du tableau : {elem}")
    new_elem = elem
    i_e = 0
    i_w = 0
    while i_e < len(elem):
        while i_e == 1:
            new_elem[i_e] = ' '
            i_e += 1
        while i_e >= 2 and i_w < len(word):
            new_elem[i_e] = word[i_w]
            i_w += 1
            i_e += 1
        i_e += 1
    i_e = len(word) + 2
    while i_e < len(elem) - 1:
        new_elem[i_e] = ' '
        i_e += 1
    return new_elem


def create_frame(text, char):
    width = len(max(text, key=len)) + 4
    #print(width)
    frame = [[char] * width] * (len(text) + 2)
    #print(frame)
    i_t = 0

    for i_f, elem in enumerate(frame, 1):
        if i_t == len(text):
            break
        frame[i_f] = fill_word(text[i_t], frame[i_f])
        #print(frame)
        i_t += 1
    print(frame[0])
    return 0

print(create_frame(['apple', 'banana', 'watermelon', 'orange'], "@"))