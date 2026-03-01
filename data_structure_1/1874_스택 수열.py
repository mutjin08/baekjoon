

n = int(input())
s = []
now = 1
answer = []
for _ in range(n):
    target = int(input())

    while now <= target:
        s.append(now)
        now += 1

        answer.append("+")

    if s[-1] == target:
        s.pop()

        answer.append("-")
    
    else:
        answer = ["NO"]
        break


for a in answer:
    print(a)
