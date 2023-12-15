from collections import deque

def solution(n, m, imps):
    out = []
    target = m

    q = deque(imps)
    while q:
        x = q.popleft()
        if len(q)>0 and x < max(q):
            q.append(x)
        else:
            out.append(x)
            if target==0:
                return len(out)
        target-=1
        target%=len(q)
    return -1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imps = list(map(int, input().split()))
    print(solution(n, m, imps))