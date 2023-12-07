def solution():
    if y%400==0:
        return 1
    if y%4==0 and y%100!=0:
        return 1
    else:
        return 0
        

y = int(input())
print(solution())