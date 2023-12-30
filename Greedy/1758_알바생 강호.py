def solution(n, limits):
    answer = 0
    limits.sort(reverse = True)
    for i in range(n):
        answer = max(answer, limits[i]*(i+1))
    return answer


n = int(input())
limits = []
for _ in range(n):
    limits.append(int(input()))
print(solution(n, limits))