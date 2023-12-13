#pypy
def spin1(arr, n, m):
    new_arr = [[0 for _ in range(m)] for _ in range(n)]
    k = min(n, m)//2
    for i in range(k):
        x, y = i, i
        for _ in range(n-1-i*2):
            new_arr[x+1][y] = arr[x][y]
            x+=1
        for _ in range(m-1-i*2):
            new_arr[x][y+1] = arr[x][y]
            y+=1
        for _ in range(n-1-i*2):
            new_arr[x-1][y] = arr[x][y]
            x-=1
        for _ in range(m-1-i*2):
            new_arr[x][y-1] = arr[x][y]
            y-=1
    return new_arr

def solution(arr, n, m, r):
    for _ in range(r):
        arr = spin1(arr, n, m)
    return arr

n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for s in solution(arr, n, m, r):
    print(*s)