def solution(n, k):
    visited = [0]*(n+1)
    p = 2
    
    while True:
        for i in range(p, n+1, p):
            if not visited[i]:
                visited[i] = 1
                k -= 1
                if k<1:
                    return i
        
        for i in range(p+1, n+1):
            if not visited[i]:
                p = i
                break


n, k = map(int, input().split())
print(solution(n, k))