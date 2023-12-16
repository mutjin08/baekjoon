# from math import gcd

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def solution(arr):
    total = 0
    n = len(arr)
    for i in range(1,n):
        for j in range(i+1, n):
            total += gcd(arr[i], arr[j])
    return total

t = int(input())
for _ in range(t):
    print(solution(list(map(int, input().split()))))