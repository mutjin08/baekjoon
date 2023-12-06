def solution():
    answer = 0
    s, e = 0, 0

    #주의
    while s!=n :
        e = s + k
        case = set()
        cnt, gift = 0, True

        for i in range(s, e):
            i %= n #주의
            case.add(rices[i])

            #주의
            if rices[i] == c:
                gift = False

        if gift:
            cnt+=1
        cnt = len(case)

        answer = max(answer, cnt)
        s+=1

    return answer

n, d, c, k = map(int, input().split())

rices = []
for _ in range(n):
    rices.append(int(input()))

print(solution())