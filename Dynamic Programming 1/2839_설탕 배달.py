def solution(n):
    if n==4:
        return -1
    elif n==3 or n==5:
        return 1
    
    dp = [-1]*(n+1)
    dp[3] = dp[5] = 1
    
    for i in range(6, n+1):
        cand = []
        if dp[i-3]>0:
            cand.append(dp[i-3])
        if dp[i-5]>0:
            cand.append(dp[i-5])
            
        if cand:
            dp[i] = min(cand)+1
    return dp[n]


n = int(input())
print(solution(n))