def solution(n, k):
    k-=1
    target = 0
    circle = [str(i) for i in range(1, n+1)]
    out = []

    while circle:
        target += k
        target %= len(circle)
        out.append(circle.pop(target))
    
    print("<"+", ".join(out)+">")

n, k = map(int, input().split())
solution(n, k)