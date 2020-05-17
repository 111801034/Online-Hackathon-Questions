import math

N = input()
N = int(N)
Group_of_students = list(map(int,input().split()))
Group_of_students.sort(reverse = True)
groups = {1: 0, 2: 0, 3: 0,4: 0}
taxis = 0
for i in range(0,N):
    groups[Group_of_students[i]] = groups[Group_of_students[i]] + 1
taxis = taxis + groups[4]
groups[4] = 0
m = min(groups[1],groups[3])
taxis = taxis + m
groups[3] = groups[3] - m
groups[1] = groups[1] - m
taxis = taxis + groups[3]
groups[3] = 0
taxis = taxis + int((groups[2]*2)/4)
groups[2] = groups[2] - (int((groups[2]*2)/4)*2)
print(groups[2])
if groups[2] == 0:
    taxis = taxis + math.ceil((groups[1])/4)
else:
    taxis = taxis + 1
    groups[1] = groups[1] - 2
    if groups[1] > 0:
        taxis = taxis + math.ceil((groups[1])/4)
groups[1] = 0
print(groups)
print(int(taxis))
