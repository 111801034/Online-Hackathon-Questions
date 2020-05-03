import copy

N = input()
N = int(N)
A = list(map(int,input().split()))
n = len(A)
hi = copy.deepcopy(A)
hi.sort()
ans = []
for i in range(0,n):
    if A[i]!=max(A):
        if sum(hi[:]) - A[i] == 2*hi[-1]:
            ans.append(i+1)
    else:
        if sum(hi[:-2]) == hi[-2]:
            ans.append(i+1)
print(len(ans))
for i in range(len(ans)):
    print("{} ".format(ans[i]), end='')
