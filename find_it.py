def find_it(seq):

    rep = 0 
    seq_rep = dict.fromkeys(seq, rep)    
    for elem in seq:
        seq_rep[elem] += 1
    odd_seq_rep = 0
    #print(seq_rep)
    odd_seq_rep = 0
    for elem in seq_rep.items():
        if elem[1] % 2 != 0:
            odd_seq_rep = elem[0]
    return odd_seq_rep

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))