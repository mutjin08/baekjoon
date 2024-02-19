from copy import deepcopy
def left(n, board):
    for x in range(n):
        cursor = 0
        for y in range(1, n):
            if board[x][y] == 0:
                continue
            temp = board[x][y]
            board[x][y] = 0

            if board[x][cursor] == 0:
                board[x][cursor] = temp
            elif board[x][cursor] == temp:
                board[x][cursor] *= 2
                cursor += 1
            else:
                cursor += 1
                board[x][cursor] = temp
    return board

def right(n, board):
    for x in range(n):
        cursor = n-1
        for y in range(n-2, -1, -1):
            if board[x][y] == 0:
                continue

            temp = board[x][y]
            board[x][y] = 0

            if board[x][cursor] == 0:
                board[x][cursor] = temp
            elif board[x][cursor] == temp:
                board[x][cursor] *= 2
                cursor -= 1
            else:
                cursor -= 1
                board[x][cursor] = temp
    return board


def up(n, board):
    for y in range(n):
        cursor = 0
        for x in range(1, n):
            if board[x][y] == 0:
                continue

            temp = board[x][y]
            board[x][y] = 0

            if board[cursor][y] == 0:
                board[cursor][y] = temp
            elif board[cursor][y] == temp:
                board[cursor][y] *= 2
                cursor += 1
            else:
                cursor += 1
                board[cursor][y] = temp
    return board

def down(n, board):
    for y in range(n):
        cursor = n-1
        for x in range(n-2, -1, -1):
            if board[x][y] == 0:
                continue

            temp = board[x][y]
            board[x][y] = 0

            if board[cursor][y] == 0:
                board[cursor][y] = temp
            elif board[cursor][y] == temp:
                board[cursor][y] *= 2
                cursor -= 1
            else:
                cursor -= 1
                board[cursor][y] = temp
    return board

def solution(n, board, cnt):
    if cnt==5:
        global answer
        answer = max(answer, max(map(max, board)))
        return

    solution(n, left(n, deepcopy(board)), cnt+1)
    solution(n, right(n, deepcopy(board)), cnt + 1)
    solution(n, up(n, deepcopy(board)), cnt + 1)
    solution(n, down(n, deepcopy(board)), cnt + 1)


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
answer = board[0][0]
solution(n, board, 0)
print(answer)