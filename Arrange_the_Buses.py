import copy

N, C, K = input().split()
N = int(N)
C = int(C)
K = int(K)
arrival_times = []
for kl in range(0,N):
    betkcksdck = input()
    betkcksdck = int(betkcksdck)
    arrival_times.append(betkcksdck)
arrival_times.sort()
print(arrival_times)
buses = 1
ti = arrival_times[0]
i = 0
capacity = 0
while(i < N):
    if ti <= arrival_times[i] <= ti+K and capacity < C:
        capacity = capacity + 1
        i = i + 1
    else:
        ti = arrival_times[i]
        buses = buses + 1
        capacity = 0
        
print(buses)
