def solution():
    word = "quack"
    dic = {'q':0,'u':0,'a':0,'c':0,'k':0,}
    for s in string:
        for i in range(1, 5):
            if dic[string[i-1]]<1:
                return -1
            else:
                dic[string[i-1]]-=1
                dic[string[i]]+=1

string = input()
print(solution())