def solution():
    answer = 0
    cnts = [0]*(max(arr)+1)

    s, e = 0, 0
    while e < n:
        if cnts[arr[e]] < k:
            cnts[arr[e]] += 1
            e+=1
        else:
            cnts[arr[s]] -= 1
            s+=1
        answer = max(answer, e - s)
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(solution())