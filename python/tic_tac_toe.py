#https://www.codewars.com/kata/525caa5c1bf619d28c000335

def chek_victory(one, two, three):
    return one if one == two == three else 0

def is_solved(board):
    is_full = 0
    for line in board:
        if all(line) == True:
            is_full += 1
    
    #check victory by line
    victory = []
    victory.append(chek_victory(board[0][0], board[0][1], board[0][2]))
    victory.append(chek_victory(board[1][0], board[1][1], board[1][2]))
    victory.append(chek_victory(board[2][0], board[2][1], board[2][2]))
    for v in victory:
        if v == 1:
            return 1
        if v == 2:
            return 2

    #check victory by column
    victory = []
    victory.append(chek_victory(board[0][0], board[1][0], board[2][0]))
    victory.append(chek_victory(board[0][1], board[1][1], board[2][1]))
    victory.append(chek_victory(board[0][2], board[1][2], board[2][2]))
    for v in victory:
        if v == 1:
            return 1
        if v == 2:
            return 2
        
    #check victory by diagonal
    victory = []
    victory.append(chek_victory(board[0][0], board[1][1], board[2][2]))
    victory.append(chek_victory(board[0][2], board[1][1], board[2][0]))
    for v in victory:
        if v == 1:
            return 1
        if v == 2:
            return 2
    return 0 if is_full == 3 else -1

print(is_solved([[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]))