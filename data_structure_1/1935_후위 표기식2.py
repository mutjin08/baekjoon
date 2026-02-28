def calculate(a, b, t):
    a, b = int(a), int(b)
    if t == "+":
        return a+b
    elif t == "-":
        return a-b
    elif t == "*":
        return a*b
    elif t == "/":
        return a/b
    else:
        return -1

from collections import deque

n = int(input())
target = list(input())

numbers = []
for _ in range(n):
    numbers.append(input())
numbers = deque(numbers)

# replace
for i in range(len(target)):
    if target[i].isalpha():
        target[i] = numbers.popleft()

s = []
for t in target:
    if t.isdigit():
        s.append(t)
    else:
        s.append(calculate(s.pop(), s.pop(), t))
    
    print(s)