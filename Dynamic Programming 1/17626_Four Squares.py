def solution(n):
    if n**0.5%1==0:
        return 1
    
    dp = [4 for _ in range(n+1)]
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[i-j**2]+1)
    return dp[n]

        
n = int(input())
print(solution(n))