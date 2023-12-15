import sys
input = sys.stdin.readline #주의

from heapq import heappush, heappop

n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(h, -x)
    elif x==0:
        if not h:
            print(0)
            continue
        print(-heappop(h))