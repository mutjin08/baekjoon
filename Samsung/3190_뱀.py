from collections import deque

def turn(c, sdir):
    if c == "D":
        return (sdir+1)%4
    elif c == "L":
        return (sdir-1)%4
def solution(n, k, board, l, cmds):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    hx, hy, sdir, time = 0, 0, 0, 0
    q = deque([(hx, hy)])
    board[hx][hy] = 1

    while True:
        time += 1
        hx += dx[sdir]
        hy += dy[sdir]

        if not (0<=hx<n and 0<=hy<n) or board[hx][hy]==1:
            return time

        if board[hx][hy] == 2:
            board[hx][hy] = 1
            q.append((hx, hy))
        elif board[hx][hy] == 0:
            board[hx][hy] = 1
            q.append((hx, hy))
            tx, ty = q.popleft()
            board[tx][ty] = 0

        if time in cmds:
            sdir = turn(cmds[time], sdir)

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x, y = list(map(int, input().split()))
    board[x-1][y-1] = 2

l = int(input())
cmds = {}
for _ in range(l):
    x, c = input().split()
    cmds[int(x)] = c

print(solution(n, k, board, l, cmds))