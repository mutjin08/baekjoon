def make_board():
    board_size = n + (3*(n-1))
    return [["*" for _ in range(board_size)] for _ in range(board_size)]

def fill_board(s, board, c):
    board_size = len(board)
    for i in range(s, board_size-s):
        for j in range(s, board_size-s):
            board[i][j] = c
    return board

def solution():
    board = make_board()
    for i in range(1, n**2//2+1):
        if i%2!=0:
            board = fill_board(i, board, " ")
        else:
            board = fill_board(i, board, "*")
    return board

n = int(input())
for s in solution():
    print("".join(s))