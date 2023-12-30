def solution(n, colors):
    dic = {}
    dic['B'], dic['R'] = 0, 0

    dic[colors[0]] = 1
    for i in range(n-1):
        if colors[i] != colors[i+1]:
            dic[colors[i+1]]+=1
    
    return min(dic['B'], dic['R'])+1



n = int(input())
colors = input()
print(solution(n, colors))