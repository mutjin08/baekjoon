def solution(n, arr):
    stack = []
    num = 1
    answer = []
    for i in range(n):
        while arr[i] >= num:
            stack.append(num)
            num += 1
            answer.append("+")
        
        if arr[i] == stack[-1]:
            stack.pop()
            answer.append("-")
        else:
            return ["NO"]
    return answer

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for s in solution(n, arr):
    print(s)