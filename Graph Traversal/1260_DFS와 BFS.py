from collections import deque

def dfs(v):
    dfs_result.append(v)
    dfs_visited[v] = 1
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    bfs_result.append(v)
    bfs_visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_result.append(i)
                bfs_visited[i]=1

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [0 for _ in range(n+1)]
bfs_visited = [0 for _ in range(n+1)]

dfs_result = []
bfs_result = []

dfs(v)
bfs(v)

print(*dfs_result)
print(*bfs_result)