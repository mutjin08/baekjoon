from math import comb

def solution(n, m):
    return comb(m,n)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solution(n, m))