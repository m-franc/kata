def make_checkered_board(n):
    line=['X' for x in range(n)]
    board = [line for y in range(n)]
    for row in range(0,n):
        for col in range(0,n):
            if (col+row) % 2 == 0:
                board[row][col]="0"
    for line in board:
        print(line)
    return board

make_checkered_board(5)