def solution(n):
    fdic = {}

    for _ in range(n):
        fname, fclass = input().split(".")

        if fclass not in fdic:
            fdic[fclass] = 1
        else:
            fdic[fclass] += 1

    for fclass in sorted(fdic):
        print(fclass, fdic[fclass])
    
    return

n = int(input())
solution(n)
