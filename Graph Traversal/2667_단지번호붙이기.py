from collections import deque
def bfs(x, y):

    q = deque([(x, y)])
    graph[x][y] = 0 #주의
    house = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx, ny))
                house += 1
    return house

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            answer.append(bfs(i, j))
answer.sort() #주의

print(len(answer))
for i in answer:
    print(i)