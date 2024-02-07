def solution(string):
    n = len(string)
    stick = 0
    cnt = 0

    #주의
    for i in range(n):
        if string[i]==")":
            if string[i-1]=="(":
                stick -= 1
                cnt += stick
            else:
                stick -= 1
                cnt += 1 #주의
        else:
            stick += 1
    return cnt

string = input()
print(solution(string))