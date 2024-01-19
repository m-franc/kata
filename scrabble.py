#https://www.codewars.com/kata/563f960e3c73813942000015/train/python

from string import ascii_uppercase as alph_up

points = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10)

#function which return the score of a word, to alleviate the script
def eval_word(letters_and_points, word):
    point = 0
    for c in word:
        point += letters_and_points[c]
    return point 

def get_best_word(points, words):
    #first, create dict to have letter and their point together
    letters_and_points = dict.fromkeys([a for a in alph_up])
    for i, p in enumerate(points):
        letters_and_points[alph_up[i]] = p
    #second, for each word, fill an array as a mirror, of their score
    points_words = []
    for word in words:
        points_words.append(eval_word(letters_and_points, word))
    #third, get the highest score, create and array with all of words which have this score
    max_point = max(points_words)
    highest_word = []
    for i, p in enumerate(points_words):
        if p == max_point:
            highest_word.append(words[i])
    #and return where - in words - the shortest of the highest_word is
    return words.index(min(highest_word, key=len))

print(get_best_word(points, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']))