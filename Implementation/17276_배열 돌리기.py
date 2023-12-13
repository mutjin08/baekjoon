from copy import deepcopy
def spin45(arr, n):
    mid = n//2

    new_arr = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if i==j:
                new_arr[i][mid] = arr[i][j]
                continue
            elif i+j==n-1:
                new_arr[mid][j] = arr[i][j]
                continue
            elif i==mid:
                new_arr[j][j] = arr[i][j]
                continue
            elif j==mid:
                new_arr[i][n-1-i] = arr[i][j]
                continue
            else:
                continue
    return new_arr

def solution(arr, n, d):
    while d<0:
        d+=360
    while d>=360:
        d-=360
    spin = d//45
    for _ in range(spin):
        arr = spin45(arr, n)
    return arr


t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for s in solution(arr, n, d):
        print(*s)