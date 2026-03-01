
brackets = input()

answer, target = 0, 0
for i in range(len(brackets)):
    if brackets[i] == "(":
        target += 1
    
    elif brackets[i] == ")":
        target -= 1
        if brackets[i-1] == "(":
            answer += target
        elif brackets[i-1] == ")":
            answer += 1
    
print(answer)