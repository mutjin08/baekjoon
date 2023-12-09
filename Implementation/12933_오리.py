def count_duck(sing, visited, start):
    quack = "quack"
    p = 0

    first_meet = 1
    duck = 0
    for i in range(start, len(sing)):
        if sing[i]==quack[p] and not visited[i]:
            visited[i] = 1

            if sing[i]=="k":
                p = 0
                if first_meet:
                    first_meet = 0
                    duck += 1
            else:
                p+=1

    return duck

def solution(sing, visited):

    #예외
    if len(sing)%5!=0 or sing[0]!="q" or sing[-1]!="k":
        return -1
    
    total_duck = 0
    for start in range(len(sing)):
        if sing[start]=="q" and not visited[start]:
            total_duck += count_duck(sing, visited, start)

    # 예외
    if not all(visited) or total_duck==0:
        return -1
    
    return total_duck

sing = input()
visited = [0]*(len(sing))
print(solution(sing, visited))