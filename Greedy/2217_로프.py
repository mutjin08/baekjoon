def solution(n, max_weights):
    answer = 0
    max_weights.sort(reverse = True)

    for i in range(n):
        answer = max(answer, max_weights[i]*(i+1))
    
    return answer


n = int(input())
max_weights = []
for _ in range(n):
    max_weights.append(int(input()))
print(solution(n, max_weights))