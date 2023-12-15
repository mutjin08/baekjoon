# readline, rstrip, 형식지정자

import sys
input = sys.stdin.readline #주의

dic = {}
total = 0

while True:
    tree = input().rstrip() #주의
    if tree == '':
        break

    total += 1
    
    if tree not in dic:
        dic[tree] = 0
    dic[tree] += 1

for tree in sorted(dic):
    print("%s %.4f" %(tree, dic[tree]/total*100))