def solution():
    answer = 0
    s, e = 0, 0
    cnt = 0

    while True:
        if e == n:
            break

        if cnt > k:
            if slst[s]%2!=0:
                cnt-=1
            s+=1
        else:
            if slst[e]%2!=0:
                cnt+=1
            e+=1
        
        if cnt<=k:
            answer = max(answer, e-s-cnt)
    
    return answer
        
n, k = map(int, input().split())
slst = list(map(int, input().split()))

print(solution())