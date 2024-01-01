def solution(n):
    dp = [0]*(n+1)
    dp[1] = dp[3] = "SK"
    dp[2] = "CY"
    
    for i in range(4, n+1):
        if dp[i-3]=="CY":
            dp[i] = "SK"
        elif dp[i-3]=="SK":
            dp[i] = "CY"
            
    return dp[n]

n = int(input())
print(solution(n))