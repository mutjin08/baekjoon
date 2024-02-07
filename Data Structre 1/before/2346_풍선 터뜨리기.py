def solution(n, nums):
    balls = [i for i in range(1, n+1)]
    out = []
    target = 0

    while balls:
        target %= len(balls)
        out.append(balls.pop(target))
        step = nums.pop(target)
        if step > 0:
            target += step-1
        elif step < 0:
            target += step
        else:
            continue

    return out
n = int(input())
nums = list(map(int, input().split()))

print(*solution(n, nums))