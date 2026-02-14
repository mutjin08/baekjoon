

def is_vps(brackets):
    score = 0
    for b in brackets:
        if b == "(":
            score += 1
        elif b == ")":
            if score > 0:
                score -=1
            else:
                return "NO"
    if score > 0:
        return "NO"
    elif score ==0:
        return "YES"
    
n = int(input())
for _ in range(n):
    print(is_vps(input()))