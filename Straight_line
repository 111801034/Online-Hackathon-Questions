N = int(input())
x_arr = list(map(int, input().rstrip().split()))
L = int(input())
Q = int(input())
for _ in range(Q):
    ab = list(map(int, input().rstrip().split()))
    a = ab[0]
    b = ab[1]
    distance = 0
    days = 0
    start = min(a,b)
    end = max(a,b)
    start = start - 1
    end = end - 1
    stay = x_arr[start]
    while(stay + L < x_arr[end]):
        for i in range(N-1,-1,-1):
            if x_arr[i] <= stay + L:
                stay = x_arr[i]
                days = days + 1
                break
    print(days+1)
