def solution(n, benefits):
  answer = []
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
  for x in range(1, n+1):
    for y in range(1, n+1):
      dp[x][y] = benefits[x-1][y-1] + dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]

  for k in range(0, n):
    for x1 in range(0, n-k):
      for y1 in range(0, n-k):
        x2, y2 = x1+k, y1+k
        answer.append(dp[x2+1][y2+1] - dp[x1][y2+1] - dp[x2+1][y1] + dp[x1][y1])

  return max(answer)

n = int(input())
benefits = []
for _ in range(n):
  benefits.append(list(map(int, input().split())))
print(solution(n, benefits))