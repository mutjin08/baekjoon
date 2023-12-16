# % 서식 문자
def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def solution(arr, x):
    total = 0
    cnt = 0
    for a in arr:
        if gcd(a, x)==1:
            total += a
            cnt += 1
    return total/cnt


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print("%.6f"%solution(arr, x))