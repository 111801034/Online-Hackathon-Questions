from collections import math
import math

def uniqueNumber(A):
    counter = Counter(A)
    commons = counter.most_common()
    return commons[-1][0]

def power(x, y, p): 
    res = 1
    x = x % p;  
    while (y > 0):  
        if (y & 1): 
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

T = input()
T = int(T)
MOD = 10**9 + 7
for t in range(0,T):
    N, K, R = input().split()
    N = int(N)
    K = int(K)
    R = int(R)
    A = list(map(int,input().split()))
    x = uniqueNumber(A)
    remainderB = 0
    fac = ((math.factorial(2*R))/(math.factorial(R)*math.factorial(R)))
    b = str(fac)
    for i in range(len(b)): 
    remainderB = ((remainderB * 10 + 
                   ord(b[i]) - 48) % 
                   (MOD - 1)); 
    print(power(x, remainderB, MOD))

#for reference visit link: https://www.geeksforgeeks.org/find-abm-where-b-is-very-large/
