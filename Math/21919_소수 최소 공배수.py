#소수들의 최소공배수는 단순히 곱하면 된다

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(arr):
    arr = list(set(arr)) #주의
    target = 1
    for a in arr:
        if is_prime(a):
            target*=a
    if target==1:
        return -1
    return target


n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))