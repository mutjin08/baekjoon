import sys
input = sys.stdin.readline

def solution():
    if max(logs) == 0:
        #주의
        return ["SAD"]
    
    # 주의
    val = sum(logs[0:x])
    cnt, max_val = 1, val
    for i in range(x, n):
        val -= logs[i-x]
        val += logs[i]
        if val > max_val:
            max_val = val
            cnt = 1
        elif val == max_val:
            cnt +=1
        else:
            continue

    return [max_val, cnt]


n, x = map(int, input().split())
logs = list(map(int, input().split()))

for i in solution():
    print(i)