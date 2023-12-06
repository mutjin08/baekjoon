def solution(logs):
    visits = []

    max_log = max(logs)
    if max_log == 0:
        return "SAD"
    
    for i in range(0, len(logs) - x):
        visits.append(sum(logs[i:i+x]))

    max_visit = max(visits)
    return max_visit, visits.count(max_visit)


n, x = map(int, input().split())
logs = list(map(int, input().split()))

for i in solution(logs):
    print(i)
