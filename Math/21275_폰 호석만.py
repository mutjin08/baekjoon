def solution(na, nb):
    cnt = 0

    min_digit = 2
    max_digit = 36
    
    for a in range(min_digit, max_digit+1):
        xa = int(na, a)
        print(na, a, xa)

na, nb = input().split()
print(solution(na, nb))