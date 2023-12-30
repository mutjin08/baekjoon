def solution(n, c):
    c.sort(reverse = True)

    free = 0
    for i in range(2, n, 3):
        free += c[i]
    
    return sum(c) - free

n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))
print(solution(n, c))