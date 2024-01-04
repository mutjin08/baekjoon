def solution(n):
    if n==3 or n==5:
        return 1
    if n==4:
        return -1
    
    dp = [-1]*(n+1)
    dp[3] = dp[5] = 1
    for i in range(6, n+1):
        if dp[i-3]>0 and dp[i-5]>0:
            dp[i] = min(dp[i-3], dp[i-5]) + 1
        elif dp[i-3]>0 and dp[i-5]<0:
            dp[i] = dp[i-3] + 1
        elif dp[i-3]<0 and dp[i-5]>0:
            dp[i] = dp[i-5] + 1
    
    return dp[n]

n = int(input())
print(solution(n))