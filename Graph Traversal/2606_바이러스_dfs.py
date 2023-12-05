def dfs(graph, visited, v):
    visited[v] = 1 #주의

    for i in graph[v]:
        if not visited[i]:
            visited[i]=1
            dfs(graph, visited, i)

    return sum(visited) - 1


n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, visited, 1))