def solution(n, p):
    tot, acc = 0, 0
    p.sort()
    for i in range(n):
        acc += p[i]
        tot += acc
    return tot
n = int(input())
p = list(map(int, input().split()))
print(solution(n, p))