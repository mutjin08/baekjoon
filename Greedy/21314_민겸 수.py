def solution(mk):
    min_val = ""
    max_val = ""

    if mk[0]=='K':
        min_val += '5'
        max_val += '5'
        mcnt = 0
    elif mk[0]=='M':
        mcnt = 1
        
    for i in range(1, len(mk)):
        if mk[i]=='K':
            if mk[i-1]=='K':
                min_val += '5'
                max_val += '5'
            elif mk[i-1]=="M":
                min_val += '1'+'0'*(mcnt-1)+'5'
                max_val += '5'+'0'*mcnt
                mcnt = 0
        elif mk[i]=="M":
            mcnt +=1
    if mcnt>0:
        min_val += '1'+'0'*(mcnt-1)
        max_val += '1'*mcnt

    return max_val, min_val


mk = input()
for s in solution(mk):
    print(s)