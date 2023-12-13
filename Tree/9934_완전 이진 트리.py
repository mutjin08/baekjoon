def make_tree(inordered, depth):
    mid = len(inordered)//2
    tree[depth].append(inordered[mid])

    if len(inordered)==1:
        return
    
    make_tree(inordered[:mid], depth+1)
    make_tree(inordered[mid+1:], depth+1)
    

k = int(input())
blst = list(map(int, input().split()))
tree = [[] for _ in range(k)]

make_tree(blst, 0)

for t in tree:
    print(*t)
