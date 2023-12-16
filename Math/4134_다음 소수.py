def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n):
    target = n #주의
    while True:
        if is_prime(target):
            return target
        target += 1


n = int(input())
for _ in range(n):
    print(solution(int(input())))