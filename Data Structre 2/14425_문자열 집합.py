def solution(strings, checks):
    answer = 0
    for check in checks:
        if check in strings:
            answer += 1
    return answer

n, m = map(int, input().split())

strings = {}
for _ in range(n):
    strings[input()] = True

checks = [] #주의
for _ in range(m):
    checks.append(input())

print(solution(strings, checks))