def solution(string):
    if len(string)%2!=0 or string[0]==")" or string[-1]=="(":
        return "NO"
    cnt = 0
    for s in string:
        if s=="(":
            cnt+=1
        elif s==")":
            if cnt<1:
                return "NO"
            cnt-=1
    if cnt>0:
        return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(solution(input()))