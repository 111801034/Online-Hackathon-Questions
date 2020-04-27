# cook your dish here

from operator import *

N= input()
N = int(N)
billtime_prices = []
for i in range(0,N):
    t, p = input().split()
    p = int(p)
    t = int(t)
    if t == 0:
        billtime_prices.append([float(p/(t+1)),t,p])
    else:
        billtime_prices.append([float(p/t),t,p])

cost = 0
billtime_prices.sort()
while(billtime_prices != []):
    if billtime_prices[0][1] == 0:
        cost = cost + billtime_prices[0][2]
        billtime_prices.remove(billtime_prices[0])
    else:
        cost = cost + billtime_prices[0][2]
        count = billtime_prices[0][1]
        while(count > 0):
            if billtime_prices != [] and len(billtime_prices) > 1:
                billtime_prices.remove(billtime_prices[len(billtime_prices)-1])
            count = count - 1
        billtime_prices.remove(billtime_prices[0])
print(cost)

