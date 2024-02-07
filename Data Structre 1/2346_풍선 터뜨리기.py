def solution(n, papers):
  balloons = []
  for i, p in enumerate(papers):
    balloons.append([i+1, p])

  pin = 0
  answer = []
  while balloons:
    pin %= len(balloons)
    i, p = balloons.pop(pin)
    answer.append(i)
    
    if p>0:
      pin += p-1
    elif p<0:
      pin += p
  return answer

n = int(input())
papers = list(map(int, input().split()))
print(*solution(n, papers))