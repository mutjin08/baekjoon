def solution(n, arr):
  s = []

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

for s in solution(n, arr):
  print(s)