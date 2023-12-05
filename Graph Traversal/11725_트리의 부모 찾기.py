from collections import deque

def bfs(v):
    visited[v] = -1
    q = deque([v])
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = v
                q.append(i)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

bfs(1)
print(visited)
