def solution(string):
    answer = ""
    now = 0
    while now < len(string):

        if string[now]=="<":
            end = now + 1
            while end<len(string) and string[end]!=">":
                end += 1
            end += 1
            answer+=string[now:end]
            now = end
        elif string[now]==" ":
            answer+=" "
            now += 1
        else:
            end = now + 1
            while end<len(string) and string[end]!="<" and string[end]!=" ":
                end += 1
            answer+="".join(reversed(string[now:end]))
            now = end
    return answer
string = input()
print(solution(string))