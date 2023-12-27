def solution(n, tips):
    tips.sort(reverse = True)
    total = 0
    for i in range(n):
        total += max(0, tips[i] - i)
    return total

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))
print(solution(n, tips))