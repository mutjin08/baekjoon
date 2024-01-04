def solution(n):
    if n==1:
        return 1
    if n==2:
        return 3
    
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 3
    for i in range(3, n+1):
        dp[i] = dp[i-2]*3 + dp[i-1]
    
    return dp[n]%10007

n = int(input())
print(solution(n))