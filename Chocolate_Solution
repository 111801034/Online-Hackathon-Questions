# cook your dish here

from operator import *
            

M = input()
M = int(M)
chocolate_limit_range = []
for i in range(0,M):
    A, B = input().split()
    A = int(A)
    B = int(B)
    chocolate_limit_range.append([A, B, i+1])
chocolates = 0
students = 0
chocolate_limit_range.sort(key=itemgetter(1))
minimum_value = chocolate_limit_range[0][1]
li = []
for i in range(0,M):
    if chocolate_limit_range[i][0] <= minimum_value:
        li.append(chocolate_limit_range[i][0])
print(max(li),len(li))
