# dictionay

def preorder(root, tree):
    if root == '.':
        return
    print(root, end="")
    preorder(tree[root][0], tree)
    preorder(tree[root][1], tree)

def inorder(root, tree):
    if root == '.':
        return
    inorder(tree[root][0], tree)
    print(root, end="")
    inorder(tree[root][1], tree)

def postorder(root, tree):
    if root == '.':
        return
    postorder(tree[root][0], tree)
    postorder(tree[root][1], tree)
    print(root, end="")

n = int(input())
tree = {}
for _ in range(n):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]

root = 'A'
preorder(root, tree)
print()
inorder(root, tree)
print()
postorder(root, tree)