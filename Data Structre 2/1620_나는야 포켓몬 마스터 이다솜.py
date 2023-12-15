# isdigit(), isalpha()
# 시간초과를 해결하기 위해 메모리를 2배로 사용한다

def solution(n, monster_id, monster_name, m, questions):
    for question in questions:
        if question.isalpha():
            print(monster_id[question])
        else:
            print(monster_name[int(question)])

n, m = map(int, input().split())
monster_id = {}
monster_name = {}
for id in range(1, n+1):
    name = input()
    monster_id[name] = id
    monster_name[id] = name

questions = []
for _ in range(m):
    questions.append(input())

solution(n, monster_id, monster_name, m, questions)