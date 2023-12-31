def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    
    dp = [0]*(n+1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))