N = input()
N = int(N)
Hire = input()
print(Hire)
list_values = []
for i in range(0,len(Hire)):
    if Hire[i] == "R":
        list_values.append(-1)
    else:
        list_values.append(0)
print(list_values)
start = 0
count = 0
li = []
for i in range(0,len(list_values)):
    count = count + list_values[i]
    if count < 0:
        li.append([count,start,i])
    else:
        start = i+1
        count = 0
li.sort()
print(li)
ans = 0
required_temp = li[0]
for i in range(0,len(list_values)):
    if required_temp[1] <= i <= required_temp[2]:
        pass
    elif list_values[i] == "0":
        ans = ans + 1
print(ans + abs(required_temp[0]))
