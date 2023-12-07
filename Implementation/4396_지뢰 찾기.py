def open_all(board):
    for i in range(n):
        for j in range(n):
            if mines[i][j]=="*":
                board[i][j]="*"
    return board

def count_mine(x, y):
    answer = 0
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and mines[nx][ny]=="*":
            answer+=1

    return str(answer)


def solution():
    mine_opened = False
    board = [["." for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if plays[i][j]==".":
                continue

            if mines[i][j]=="*":
                mine_opened = True
            else:
                board[i][j] = count_mine(i, j)
        
    if mine_opened:
        return open_all(board)
    
    return board


n = int(input())
mines = []
plays = []

for _ in range(n):
    mines.append(list(input()))
for _ in range(n):
    plays.append(list(input()))

for s in solution():
    print("".join(s))