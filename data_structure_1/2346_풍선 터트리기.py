n = int(input())

index = 1
balloons = []
for paper in map(int, input().split()):
    balloons.append([index, paper])
    index += 1

pin = 0
answer = []

while balloons:
    index, paper = balloons.pop(pin)
    answer.append(index)

    if not balloons:
        break

    pin += paper
    if paper > 0:
        pin -= 1
    pin %= balloons
"""    while pin >= len(balloons):
        pin -= len(balloons)
    while pin < 0:
        pin += len(balloons)
"""

print(" ".join(map(str, answer)))
    
    

