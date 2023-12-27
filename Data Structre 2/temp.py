
n, m = map(int,input().split())
dic = {}

for idx in range(1, n+1):
    idx = str(idx)
    name = input().strip()
    dic[idx] = name
    dic[name] = idx

for _ in range(m):
    target = input().strip()
    print(dic[target])