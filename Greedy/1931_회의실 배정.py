def solution(n, infos):
    infos.sort(key = lambda x : (x[1], x[0]))
    open = 0
    cnt = 0
    for i in range(n):
        if open >= infos[i][0]:
            open = infos
            cnt += 1


n = int(input())
infos = []
for _ in range(n):
    infos.append(list(map(int, input().split())))
print(solution(n, infos))