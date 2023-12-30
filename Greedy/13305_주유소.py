def solution(n, dist, cost):
    total, mincost = 0, cost[0]
    for i in range(n-1):
        if mincost > cost[i]:
            mincost = cost[i]
        total += mincost*dist[i]
    return total

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
print(solution(n, dist, cost))