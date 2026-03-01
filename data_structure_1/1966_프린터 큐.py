def get_order(n, m, papers):
    answer = 1
    while papers:
        index, priority = zip(*papers)

        if priority[0] == max(priority):
            if index[0] == m:
                return answer
            
            papers.pop(0)
            answer += 1
        else:
            papers.append(papers.pop(0))




t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    papers = list(enumerate(map(int, input().split())))

    print(get_order(n, m, papers))