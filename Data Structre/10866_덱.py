from collections import deque

def solution(cmds):
    d = deque([])
    for cmd in cmds:
        if len(cmd)>1:
            x = cmd[1]
        cmd = cmd[0]

        if cmd=="push_front":
            d.appendleft(x)
        elif cmd=="push_back":
            d.append(x)
        elif cmd=="pop_front":
            if len(d)<1:
                print(-1)
            else:
                print(d.popleft())
        elif cmd=="pop_back":
            if len(d)<1:
                print(-1)
            else:
                print(d.pop())
        elif cmd=="size":
            print(len(d))
        elif cmd=="empty":
            if len(d)<1:
                print(1)
            else:
                print(0)
        elif cmd=="front":
            if len(d)<1:
                print(-1)
            else:
                print(d[0])
        elif cmd=="back":
            if len(d)<1:
                print(-1)
            else:
                print(d[-1])
        else:
            continue

n = int(input())
cmds = []
for _ in range(n):
    cmds.append(input().split())

solution(cmds)