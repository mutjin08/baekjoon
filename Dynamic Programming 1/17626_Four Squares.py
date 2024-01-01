from itertools import combinations
def solution(n):
    if (n**0.5)%1==0:
        return 1
        
    nums = []
    for i in range(1, int(n**0.5)+1):
        nums.append(i**2)
    
    for i in range(2, 5):
        for case in combinations(nums, i):
            if sum(case)==n:
                return i
    return -1

n = int(input())
print(solution(n))