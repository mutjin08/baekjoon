def solution(n, loss):
    loss.sort()

    if n%2!=0:
        total = loss.pop()
    elif n%2==0:
        total = 0
    
    n = len(loss)
    for i in range(n//2):
        total = max(loss[i]+loss[n-i-1], total)
    
    return total

n = int(input())
loss = list(map(int, input().split()))
print(solution(n, loss))