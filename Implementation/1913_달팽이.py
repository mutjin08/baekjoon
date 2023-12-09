def make_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def fill_board(board, n):
    num = n**2
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for p in range(n//2+1):
        x, y = p, p
        temp = num
        num -= 1
        for i in range(4):
            for _ in range(n-1 - 2*p):
                x += dx[i]
                y += dy[i]
                board[x][y] = num
                num -= 1
        num+=1
        board[p][p] = temp
    return board

def find_target(board, n, target):
    for i in range(n):
        for j in range(n):
            if board[i][j]==target:
                return [i+1, j+1]

def solution():
    board = make_board(n)
    board = fill_board(board, n)
    board.append(find_target(board, n, target))
    return board

n = int(input())
target= int(input())

for s in solution():
    print(*s)