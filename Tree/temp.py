# reverse inordered result

def solution(log, depth):
    root = len(log)//2
    tree[depth].append(log[root])

    if len(log)==1:
        return
    
    solution(log[:root], depth+1)
    solution(log[root+1:], depth+1)


k = int(input())
log = list(map(int, input().split()))
tree = [[] for _ in range(k)]

solution(log, 0)
for t in tree:
    print(*t)