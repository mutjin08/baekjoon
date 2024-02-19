def roll(dice, cmd):
    v1, v2, v3, v4, v5, v6 = dice
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if cmd == 1:
        return [v4, v2, v1, v6, v5, v3]
    elif cmd == 2:
        return [v3, v2, v6, v1, v5, v4]
    elif cmd == 3:
        return [v5, v1, v3, v4, v6, v2]
    elif cmd == 4:
        return [v2, v6, v3, v4, v1, v5]


def solution(n, m, x, y, k, board, cmds):
    answer = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    dice = [0, 0, 0, 0, 0, 0]
    nx, ny = x, y
    for cmd in cmds:
        nx += dx[cmd - 1]
        ny += dy[cmd - 1]

        if not (0 <= nx < n and 0 <= ny < m):
            nx -= dx[cmd - 1]
            ny -= dy[cmd - 1]
            continue

        dice = roll(dice, cmd)

        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0

        answer.append(dice[0])
    return answer


n, m, x, y, k = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
cmds = list(map(int, input().split()))

for s in solution(n, m, x, y, k, board, cmds):
    print(s)