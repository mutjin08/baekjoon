from collections import deque

n = int(input())

cards = deque([i for i in range(n, 0, -1)])

while len(cards)>1:
    cards.pop()
    cards.appendleft(cards.pop())

print(cards[0])