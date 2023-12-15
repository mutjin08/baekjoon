import sys
input = sys.stdin.readline #주의

from heapq import heappush, heappop

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x!=0:
        heappush(h, [abs(x), x])
    else:
        if len(h)<1:
            print(0)
        else:
            abs_num, org_num = heappop(h)
            print(org_num)
