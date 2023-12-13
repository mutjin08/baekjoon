def suffle_back(after_cards, d):
    before_cards = [0]*n
    for i in range(n):
        before_idx, after_idx = d[i]-1, i
        before_cards[before_idx] = after_cards[after_idx]
    return before_cards


def solution(n, k, s, d):
    for _ in range(k):
        s = suffle_back(s, d)
    return s


n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

print(*solution(n, k, s, d))