def is_point(graph, k):
    if len(graph[k])<2:
        return "no"
    else:
        return "yes"

def is_line():
    return "yes"

def solution(graph, qlst):
    for t, k in qlst:
        if t==1:
            print(is_point(graph, k))
        elif t==2:
            print(is_line())
        else:
            continue

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = int(input())
qlst = []
for _ in range(n-1):
    qlst.append(map(int, input().split()))

solution(graph, qlst)