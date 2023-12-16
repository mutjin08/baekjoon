def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    erase = [0]*(n+1)
    p = 2
    last = -1
    while True:
        for i in range(p, n+1, p):
            erase[i] = 1
            k-=1
            if k<1:
                return i
        for i in range(p+1, n):
            if erase[i]==0:
                p = i
                continue

n, k = map(int, input().split())
print(solution(n, k))