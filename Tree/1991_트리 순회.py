def preorder(v):
    if v!=".":
        print(v, end = "")
        preorder(graph[v][0])
        preorder(graph[v][1])

def inorder(v):
    if v!=".":
        inorder(graph[v][0])
        print(v, end = "")
        inorder(graph[v][1])

def postorder(v):
    if v!=".":
        postorder(graph[v][0])
        postorder(graph[v][1])
        print(v, end = "")

n = int(input())

graph = {}
for _ in range(n):
    a, b, c = input().split()
    graph[a] = [b, c]

preorder('A')
print()
inorder('A')
print()
postorder('A')