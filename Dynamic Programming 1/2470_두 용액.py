def solution(m, n):
    dp = [[0 for _ in range(30)] for _ in range(30)]
    for i in range(1, m+1):
        for j in range(1, i+1):
            if j==1:
                dp[i][j] = i
            elif i==j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp)
    print(dp[m][n])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solution(m, n))