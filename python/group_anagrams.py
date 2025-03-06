#https://www.codewars.com/kata/537400e773076324ab000262/train/python

from collections import Counter
from itertools import permutations

def group_anagrams(words):
    words_sorted = list(map(sorted, words))
    words_sorted = list(map("".join, words_sorted))
    groups_words_sd = []
    groups_words = []
    for i, word_sd in enumerate(words_sorted):
        group_word_sd = []
        group_word = []
        if i == 0:
            group_word_sd.append(word_sd)
            groups_words_sd.append(group_word_sd)
            group_word.append(words[i])
            groups_words.append(group_word)
        else:
            o = 0
            while o < len(groups_words_sd):
                if groups_words_sd[o][0] == word_sd:
                    groups_words_sd[o].append(word_sd)
                    groups_words[o].append(words[i])
                    break
                o += 1
            if o == len(groups_words_sd):
                groups_words_sd.append([word_sd])
                groups_words.append([words[i]])
    return groups_words

def group_anagrams(words):
    groups = dict()
    for word in words:
        key = tuple(sorted(word))
        print(groups)
        print(key)
        try:
            groups[key].append(word)
        except:
            groups[key] = [word]
    return [v for v in groups.values()]

print(group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))