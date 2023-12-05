#https://www.codewars.com/kata/56684677dc75e3de2500002b/train/python

def comfortable_word(word):
    left = "qwertasdfgzxcvb"
    fst_lft_meet = 0
    ix_last_lft = 0
    fst_rgt_meet = 0
    ix_last_rgt = 0
    for i, c in enumerate(word):
        # when meeting left char for the first time
        if c in left and fst_lft_meet == 0:
            ix_last_lft = i
            fst_lft_meet = 1
        # when meeting left char
        elif c in left and fst_lft_meet != 0: 
            if i == ix_last_lft + 1:
                return False
            ix_last_lft = i
        # when meeting right char for the first time
        if c not in left and fst_rgt_meet == 0:
            ix_last_rgt = i
            fst_rgt_meet = 1
        # when meeting right char
        elif c not in left and fst_rgt_meet != 0: 
            if i == ix_last_rgt + 1:
                return False
            ix_last_rgt = i
    return True

print(comfortable_word("abcdefghijkl"))
