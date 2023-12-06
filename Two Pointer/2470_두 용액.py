def solution():
    vals.sort()

    s, e = 0, n-1
    min_dist = 2000000000
    while s<e:
        now_sum = vals[s] + vals[e]
        now_dist = abs(now_sum)
        
        if now_dist < min_dist:
            min_dist = now_dist
            answer = [vals[s], vals[e]]

            if now_dist==0:
                break
        
        if now_sum < 0:
            s+=1
        else:
            e-=1

    return answer
            

n = int(input())
vals = list(map(int, input().split()))
print(*solution())