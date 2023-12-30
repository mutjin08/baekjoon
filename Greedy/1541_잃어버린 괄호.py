from re import split
def solution(raw_exp):
    exps = raw_exp.split('-')
    
    total = []
    for exp in exps:
        total.append(sum(map(int, exp.split('+'))))
    return total[0] - sum(total[1:])

exp = input()
print(solution(exp))