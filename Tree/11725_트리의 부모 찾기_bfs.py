from collections import deque

def solution(n, tree):
    visited = [0 for _ in range(n+1)]
    visited[1] = -1 #root

    q = deque([1])
    while q:
        v = q.popleft()
        for i in tree[v]:
            if not visited[i]:
                visited[i] = v
                q.append(i)

    return visited[2:]


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for s in solution(n, tree):
    print(s)