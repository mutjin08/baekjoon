def solution(string):
    stack = []
    answer = 0
    val = 1
    for i in range(len(string)):
        if string[i]=="(":
            stack.append("(")
            val *= 2
        elif string[i]=="[":
            stack.append("[")
            val *= 3
        elif string[i]==")":
            if not stack or stack[-1]=="[":
                return 0
            #주의
            if string[i-1]=="(":
                answer += val
            #주의
            stack.pop()
            val //= 2
        elif string[i]=="]":
            if not stack or stack[-1]=="(":
                return 0
            if string[i-1]=="[":
                answer += val
            stack.pop()
            val //= 3
        else:
            continue
    
    #주의
    if stack:
        return 0
    return answer

string = input()
print(solution(string))