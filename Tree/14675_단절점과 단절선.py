# is_node 판단
# root노드 or leaf노드

# 시간초과 해결
# 1. solution 함수 없이 입력과 동시에 계산
# 2. input 대신 sys.stdin.readline 활용

import sys
input = sys.stdin.readline

def is_node(k, tree):
    if len(tree[k])<2:
        return "no"
    return "yes"

def is_edge(k, tree):
    return "yes"

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
queries = []
for _ in range(q):
    t, k = map(int, input().split())
    if t==1:
        print(is_node(k, tree))
    elif t==2:
        print(is_edge(k, tree))