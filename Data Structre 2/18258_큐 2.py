import sys
input = sys.stdin.readline #주의
from collections import deque

def solution(cmds):
    stack = deque([])
    for cmd in cmds:
        if len(cmd)>1:
            x = cmd[1]
        cmd = cmd[0]

        if cmd=="push":
            stack.append(x)
        elif cmd=="pop":
            if len(stack)<1:
                print(-1)
            else:
                print(stack.popleft())
        elif cmd=="size":
            print(len(stack))
        elif cmd=="empty":
            if len(stack)<1:
                print(1)
            else:
                print(0)
        elif cmd=="front":
            if len(stack)<1:
                print(-1)
            else:
                print(stack[0])
        elif cmd=="back":
            if len(stack)<1:
                print(-1)
            else:
                print(stack[-1])
        else:
            continue

n = int(input())
cmds = []
for _ in range(n):
    cmds.append(input().split())

solution(cmds)