from collections import deque
def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

    return sum(visited)-1 #주의

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, visited, 1))