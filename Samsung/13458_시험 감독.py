def solution(n, a, b, c):
    answer = 0
    for room in a:
        # 총감독관
        answer += 1
        if room <= b:
            continue
        else:
            room -= b
        # 부감독관
        answer += room//c
        if room % c != 0:
            answer += 1

    return answer

n = int(input())
a = list(map(int, input().split()))
b, c = list(map(int, input().split()))
print(solution(n, a, b, c))