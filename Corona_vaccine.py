# cook your dish here

import math
    

n, d, k = input().split()
n = int(n)
d = int(d)
k = int(k)
vaccine_powers = list(map(int, input().split()))
print(vaccine_powers)
trials = 0
while(trials <= k):
    vaccine_powers.sort(reverse = True)
    power = vaccine_powers[0]
    if power >= d:
        d = 0
        trials = trials + 1
        break
    else:
        d = d - power
        vaccine_powers[0] = int(math.floor(vaccine_powers[0]/2))
        trials = trials + 1
if trials > k:
    print(-1)
else:
    print(trials)
