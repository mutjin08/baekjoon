def solution():
    for sex, num in students:
        #남학생
        if sex == 1:
            for i in range(1,n+1):
                if i%num==0:
                    switches[i]=0 if switches[i]==1 else 1
            continue
        
        #여학생
        if sex == 2:
            switches[num]=0 if switches[num]==1 else 1

            for i in range(1, n+1):
                s, e = num - i, num + i

                if s<1 or e>n:
                    break

                if switches[s]!=switches[e]:
                    break

                switches[s]=0 if switches[s]==1 else 1
                switches[e]=0 if switches[e]==1 else 1

    # 주의
    return [switches[i:i+20] for i in range(1, n+1, 20)]

n = int(input())
switches = [-1]+list(map(int, input().split()))

m = int(input())
students = []
for _ in range(m):
    students.append(list(map(int, input().split())))

for s in solution():
    print(*s)