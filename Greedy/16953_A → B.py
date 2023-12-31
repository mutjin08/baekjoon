def  solution(a, b):
    if b < a:
        return -1

    cnt = 0
    while b > a:
        last = b%10
        if last == 1:
            b //= 10
            cnt += 1
        elif last % 2 == 0:
            b //= 2
            cnt += 1
        else:
            return -1
    
    if b!=a:
        return -1
    return cnt + 1

a, b = map(int, input().split())
print(solution(a, b))