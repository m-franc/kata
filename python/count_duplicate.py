#https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

def duplicate_count(text):
    count = 0
    text = text.lower()
    text_nb_occ = dict.fromkeys(text, 0)
    for c in text:
        text_nb_occ[c] += 1 
    for nb_occ in text_nb_occ.items():
        if nb_occ[1] > 1:
            count += 1
    return count

print(duplicate_count("abcdeaa"))