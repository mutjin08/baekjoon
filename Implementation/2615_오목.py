def is_omok(n, board, x, y):
    color = board[x][y]
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    for i in range(4):
        cnt = 0
        nx, ny = x, y

        if 0<=nx-dx[i]<n and 0<=ny-dy[i]<n and board[nx-dx[i]][ny-dy[i]]==color:
            continue

        while 0<=nx<n and 0<=ny<n and board[nx][ny]==color:
            cnt+=1
            nx += dx[i]
            ny += dy[i]

        if cnt==5:
            return True
    return False

def solution(n, board):
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                continue
            if is_omok(n, board, i, j):
                return [i, j]
    return [-1, -1]

n = 19
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

x, y = solution(n, board)
if x==-1:
    print(0)
else:
    print(board[x][y])
    print(x+1, y+1)