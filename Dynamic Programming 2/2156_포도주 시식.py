def solution(n, amts):
  amts = [0]+amts
  if n==1:
    return amts[1]
  if n==2:
    return amts[1] + amts[2]
  
  dp = [0]*(n+1)
  dp[1], dp[2] = amts[1], amts[1]+amts[2]
  for i in range(3, n+1):
    # dp[i] = max(dp[i-3]+amts[i-1], dp[i-2]) + amts[i]
    dp[i] = max(dp[i-3]+amts[i-1]+amts[i], dp[i-2]+amts[i], dp[i-1])
  
  return dp[n]

n = int(input())
amts = []
for _ in range(n):
  amts.append(int(input()))
print(solution(n, amts))