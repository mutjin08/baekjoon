def solution(n, cmds):
    trains = [[0 for _ in range(20)] for _ in range(n)]

    for cmd in cmds:
        if len(cmd)>2:
            x = cmd[2]-1
        cmd, i = cmd[0], cmd[1] - 1
        
        if cmd==1:
            if not trains[i][x]:
                trains[i][x]=1
        elif cmd==2:
            if trains[i][x]:
                trains[i][x]=0
        elif cmd==3:
            trains[i] = [0] + trains[i][:19]
        elif cmd==4:
            trains[i] = trains[i][1:] + [0]
        else:
            continue
    
    for i in range(n):
        trains[i] = "".join(map(str,trains[i]))
    return len(set(trains))

n, m = map(int, input().split())
cmds = []
for _ in range(m):
    cmds.append(list(map(int, input().split())))

print(solution(n, cmds))