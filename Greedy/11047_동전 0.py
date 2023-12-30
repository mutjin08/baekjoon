def solution(n, k, a):
    a.sort(reverse = True)

    cash, coin = k, 0
    for i in range(n):
        coin += cash//a[i]
        cash %= a[i]
    return coin

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
print(solution(n, k, a))