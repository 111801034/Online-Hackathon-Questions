def minSwapsAscend(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1]) 
    vis = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans

def minSwapsDescend(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1])
    print(arrpos)
    vis = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == n-i-1:
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = n - arrpos[j][0] - 1
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 

def double_hashing(arr):
    N = len(arr)
    hash = {}
    for i in range(N):
        hash[i] = arr[i]
    tempAscend = sorted(arr)
    temp = [i+1 for i in range(N)]
    hash_ = {}
    for i in range(N):
        hash_[tempAscend[i]] = temp[i]
    final_arr = []
    for i in range(N):
        final_arr.append(hash_[hash[i]])
    return final_arr

    
def solution():
    # Write your code here
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    final_arr = double_hashing(arr)
    print(min(minSwapsAscend(final_arr), minSwapsDescend(final_arr)))


# T = int(input())
# for _ in range(T):
solution()
