from heapq import heappush, heappop

n = int(input())
h = [] #크기가 n인 heap
for _ in range(n):
    for num in map(int, input().split()):
        if len(h)<n:
            heappush(h, num)
        else:
            if h[0] < num:
                heappop(h)
                heappush(h, num)

print(h[0])
