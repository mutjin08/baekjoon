def calculate(a, b, op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return a/b
    else:
        return -1

def postfix(elst):
    stack = []

    for i in range(len(elst)):
        if elst[i] in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            stack.append(calculate(a, b, elst[i]))
        else:
            stack.append(elst[i])

    return "{:.2f}".format(stack[0])

def convert(exp, val):
    elst = list(exp)
    p = 0

    dic = {}
    for i in range(len(exp)):
        if exp[i] in ["+", "-", "*", "/"]:
            continue

        if exp[i] not in dic:
            dic[exp[i]]=val[p]
            p+=1

        elst[i] = dic[exp[i]]

    return elst

def solution(exp, val):
    elst = convert(exp, val)
    return postfix(elst)

n = int(input())
exp = input()
val = []
for _ in range(n):
    val.append(int(input()))

print(solution(exp, val))