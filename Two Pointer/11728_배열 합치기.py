def solution(a, b):
    result = [] #주의
    ap, bp = 0, 0

    while ap<n and bp<m:
        if a[ap] < b[bp]:
            result.append(a[ap])
            ap+=1
        else:
            result.append(b[bp])
            bp+=1
    
    while ap<n:
        result.append(a[ap])
        ap+=1

    while bp<m:
        result.append(b[bp])
        bp+=1
    
    return result

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*solution(a, b))

