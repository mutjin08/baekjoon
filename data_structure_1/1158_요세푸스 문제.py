
n, k = map(int, input().split())

members = [str(i) for i in range(1, n+1)]
answers = []

target = 0
while members:
    target = (target+k-1)%len(members)
    #target = (start+k)%len(members)-1
    answers.append(members.pop(target))


print("<"+", ".join(answers)+">")