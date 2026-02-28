n = int(input())

balloons = []
for index, paper in enumerate(map(int, input().split())):
    balloons.append([index+1, paper])
"""index = 1
for paper in map(int, input().split()):
    balloons.append([index, paper])
    index += 1"""

pin = 0
answer = []

while balloons:
    pin %= len(balloons)

    index, paper = balloons.pop(pin)
    answer.append(index)

    if paper > 0:
        pin += paper - 1
    elif paper <=0:
        pin += paper

"""    while pin >= len(balloons):
        pin -= len(balloons)
    while pin < 0:
        pin += len(balloons)
"""

print(" ".join(map(str, answer)))
    
    

