def solution(n, arr):
    dp = [0]*(n+1)
    for i in range(n):
        t, p = arr[i]
        for j in range(i+t, n+1):
            dp[j] = max(dp[j], dp[i]+p)
    return dp[-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(solution(n, arr))