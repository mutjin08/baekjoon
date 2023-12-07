def bingo_count(board, x, y):
    answer = 0

    #아래대각선
    if x==y and sum([board[i][i] for i in range(n)])==n:
        answer += 1
    
    #위대각선
    if x+y==n-1 and sum([board[i][n-i-1] for i in range(n)])==n:
        answer += 1
    #가로
    if sum(board[x])==n:
        answer += 1

    #세로
    if sum([board[i][y] for i in range(n)])==n:
        answer += 1
    
    return answer

def solution():
    answer = 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    before, after = False, False

    for i in range(n**2):
        x, y = writes[calls[i]]
        
        before = bingo_count(board, x, y)
        
        board[x][y] = 1
        after = bingo_count(board, x, y)

        answer += after + before

        if answer>=3:
            return i+1

writes = {}
calls = []
n = 5

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        writes[temp[j]] = [i,j]

for _ in range(n):
    calls.extend(list(map(int, input().split())))

print(solution())