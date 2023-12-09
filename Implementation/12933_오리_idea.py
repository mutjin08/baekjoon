def solution():
    dic = {'q':0,'u':0,'a':0,'c':0,'k':0,}
    for s in string:
        if s=="q":
            dic["q"]+=1
        elif s=="u":
            if dic["q"]>0:
                dic["q"]-=1
                dic["u"]+=1
            else:
                return -1
        elif s=="a":
            if dic["u"]>0:
                dic["u"]-=1
                dic["a"]+=1
            else:
                return -1
        elif s=="c":
            if dic["a"]>0:
                dic["a"]-=1
                dic["c"]+=1
            else:
                return -1
        elif s=="k":
            if dic["c"]>0:
                dic["c"]-=1
                dic["k"]+=1
            else:
                return -1
        else:
            continue
    return dic["k"]

string = input()
print(solution())