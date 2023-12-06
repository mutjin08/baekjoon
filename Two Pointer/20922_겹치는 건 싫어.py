
def solution():
    dic = {}
    for a in arr:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    
    max_cnt = max(dic.values())
    max_len = n
    while max_cnt > k:
        max_len -= 1
        for i in range(0, n - max_len):
    return max_len

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(solution())