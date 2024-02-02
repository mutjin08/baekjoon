def solution(n, costs):
  for i in range(1, n):
    costs[i][0] = min(costs[i-1][1],costs[i-1][2])+costs[i][0]
    costs[i][1] = min(costs[i-1][0],costs[i-1][2])+costs[i][1]
    costs[i][2] = min(costs[i-1][0],costs[i-1][1])+costs[i][2]
  return min(costs[n-1])


n = int(input())
costs = []
for _ in range(n):
  costs.append(list(map(int, input().split())))
print(solution(n, costs))