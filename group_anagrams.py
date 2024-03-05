#https://www.codewars.com/kata/537400e773076324ab000262/train/python

from collections import Counter
from itertools import permutations

def group_anagrams(words):
    words_sorted = []
    for word in words:
        words_sorted.append("".join(sorted(word)))
    words_sorted_cat = Counter(words_sorted)
    groups_words = []
    group_words = []
    i = 0
    for catword in words_sorted_cat.items():
        print(catword[0])
        all_anagrams = permutations(catword[0])
        for o in range(catword[1]):
            print(["".join(w) for w in all_anagrams])
            for anagram in ["".join(w) for w in all_anagrams]:
                group_words.append(words[i])
                i += 1
        groups_words.append(group_words)
    print(groups_words)
    return 0

print(group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))