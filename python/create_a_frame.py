#https://www.codewars.com/kata/5672f4e3404d0609ec00000a/train/python


def fill_mid_line(text, char, width):
    mid_line = []
    for elem in text:
        elem = char + ' ' + elem + (' ' * (width - len(elem) - 3)) + char
        mid_line.append(elem)
    return mid_line

def frame(text, char):
    width = len(max(text, key=len)) + 4
    frame = fill_mid_line(text, char, width) 
    frame.insert(0, char*width)
    frame.insert(len(frame), char*width)
    frame_rdy_to_str = list(map(lambda elem: elem + '\n', frame))
    return "".join(frame_rdy_to_str)[:-1]

print(frame(['apple', 'banana', 'watermelon', 'orange'], "@"))