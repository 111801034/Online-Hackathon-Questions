T = input()
T = int(T)
for t in range(0,T):
    A = list(map(int,input().split()))
    n = A[0]
    A.remove(n)
    A.sort()
    break_points = []
    count = 0
    for i in range(0,n-1):
        if A[i+1] - A[i] != 1:
            break_points.append(i)
    l = len(break_points)
    if l == 0:
        print(n)
    else:
        li = []
        count = 0
        for h in range(0,n):
            count = count + 1
            if h in break_points:
                li.append(count)
                count = 0
        li.append(count)
        print(min(li))
