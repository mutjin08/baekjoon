import sys
input = sys.stdin.readline

from collections import deque
dq = deque([])

n = int(input())
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        x = cmd[1]
    cmd = cmd[0]

    if cmd == "push_front":
        dq.appendleft(x)
    elif cmd == "push_back":
        dq.append(x)
    elif cmd == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)