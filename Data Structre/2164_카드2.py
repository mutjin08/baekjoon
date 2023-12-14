from collections import deque
#위-아래

def solution(n):
    cards = deque([i for i in range(1, n+1)])

    for _ in range(n-1):
        cards.popleft()
        cards.append(cards.popleft())
    
    return cards[0]

n = int(input())
print(solution(n))