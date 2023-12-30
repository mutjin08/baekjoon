def solution(cash):
    coin = 0
    while cash > 0:
        if cash%5==0:
            coin += cash//5
            cash %= 5
            break
        coin += 1
        cash -= 2
    if cash < 0:
        return -1
    return coin
n = int(input())
print(solution(n))