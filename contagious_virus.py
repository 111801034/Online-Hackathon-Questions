
import copy
import numpy as np

N, K, T = input().split()
N = int(N)
K = int(K)
T = int(T)
A = input()
B = list(map(int,input().split()))
B.sort()
li = []
for i in range(0,N):
    if A[i] == "v":
        li.append(1)
    else:
        li.append(0)
time = 0
while(time < T):
    temp = np.zeros(N)
    for i in range(0,N):
        if li[i] != 0:
            for j in range(0,K):
                if 0 <= i+B[j] <= N-1:
                    temp[i+B[j]] = temp[i+B[j]] + li[i]
    li = copy.deepcopy(temp)
    print(li)
    time = time + 1
print(li)
    
    
            
            
        
        
    

        
            
        
