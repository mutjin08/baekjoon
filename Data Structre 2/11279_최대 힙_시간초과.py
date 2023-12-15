def solution(ops):
    arr = []
    for op in ops:
        if op > 0:
            arr.append(op)
        elif op == 0:
            if not arr:
                print(0)
                continue
            max_val = max(arr)
            max_idx = arr.index(max_val)
            print(arr.pop(max_idx))
        else:
            continue

n = int(input())
ops = []
for _ in range(n):
    ops.append(int(input()))

solution(ops)