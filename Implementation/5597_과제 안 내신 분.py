def solution():
    answer = []
    for i in range(1, 31):
        if students[i]==0:
            answer.append(i)
    return answer

students = [0]*31
for _ in range(28):
    students[int(input())]=1

for i in solution():
    print(i)