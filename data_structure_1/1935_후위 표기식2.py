def calculate(e, b, a):
    if e == "+":
        return a + b
    elif e == "-":
        return a - b
    elif e == "*":
        return a * b
    elif e == "/":
        return a / b
    else:
        return -1

n = int(input())
exp = input()

alp_to_num = {}
s = []
for e in exp:
    if e.isalpha():
        if e not in alp_to_num:
            alp_to_num[e] = float(input())
        s.append(alp_to_num[e])
    else:
        s.append(calculate(e, s.pop(), s.pop()))
    

print("{0:.2f}".format(s[0]))