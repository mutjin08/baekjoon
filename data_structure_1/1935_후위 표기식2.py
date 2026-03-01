def calculate(b, a, operator):

    if operator == "+":
        return a+b
    
    elif operator == "-":
        return a-b

    elif operator == "*":
        return a*b

    elif operator == "/":
        return a/b

    else:
        return -1



n = int(input())
exp = input()

#replace

alp_to_num = {}
pin = 0
for _ in range(n):
    alp_to_num[exp[pin]] = float(input())

    pin+=1
    while pin<len(exp) and not exp[pin].isalpha():
        pin+=1


s = []
for e in exp:
    if e.isalpha():
        s.append(alp_to_num[e])
    else:
        s.append(calculate(s.pop(), s.pop(), e))

print("{0:.2f}".format(s[0]))