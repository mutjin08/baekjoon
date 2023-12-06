from collections import deque

# 폭발
def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]=="O":
                graph[nx][ny]="."

# 플레이
def play(t):
    if t%3==0:
        q = deque([])
        for i in range(r):
            for j in range(c):
                if graph[i][j]=="O":
                    q.append((i, j))
    if t%3==1:
        return
    bfs(q)

r, c, n = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(n):
    play(t)