
def solution(n, bnums):
    q = [i for i in range(n)]
    out = []

    target = 0
    while q:
        x = q.pop(target)
        out.append(x+1)

        if not q:
            return out
        
        target += bnums.pop(target)
        target %= len(q)
    
    return -1

n = int(input())
bnums = list(map(int, input().split()))
print(*solution(n, bnums))