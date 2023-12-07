#주의
import sys
input = sys.stdin.readline

def solution():
    answer = 0
    s, e = 0, 0

    #주의
    while s!=n :
        e = s + k
        case = set()
        gift = True

        for i in range(s, e):
            i %= n #주의
            case.add(rices[i])

            #주의
            if rices[i] == c:
                gift = False

        cnt = len(case)
        if gift:
            cnt+=1

        answer = max(answer, cnt)
        
        if answer == k+1:
            return answer
        s+=1
        
    return answer

n, d, c, k = map(int, input().split())

rices = []
for _ in range(n):
    rices.append(int(input()))

print(solution())