import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, now):
    for v in graph[now]:
        if not visited[v]:
            visited[v] = now
            dfs(graph, visited, v)


n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = -1
dfs(graph, visited, 1)

for i in range(2,n+1):
    print(visited[i])