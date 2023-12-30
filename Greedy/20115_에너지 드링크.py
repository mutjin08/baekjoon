def solution(n, x):
    x.sort()
    total = x[-1]
    for i in range(n-1):
        total += x[i]/2
    return total

n = int(input())
x = list(map(int, input().split()))
print(solution(n, x))