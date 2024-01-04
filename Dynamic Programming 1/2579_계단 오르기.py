def solution(n, scores):
    scores = [0] + scores
    if n==1:
        return scores[1]
    if n==2:
        return scores[1]+scores[2]

    dp = [0]*(n+1)
    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+scores[i-1], dp[i-2]) + scores[i]
    return dp[n]


n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
print(solution(n, scores))