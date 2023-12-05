from collections import deque
def bfs(v):
    visited = [0 for _ in range(n+1)]
    
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return sum(visited) - 1

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

childs = [0 for _ in range(n+1)]
for i in range(1, n+1):
    childs[i] = bfs(i)

max_child = max(childs)
answer = []
for i in range(1, n+1):
    if childs[i] == max_child:
        answer.append(i)
print(*answer)