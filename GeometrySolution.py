n = int(input()) #number of rulers
arr = list(map(int, input().rstrip().split()))

arr = sorted(arr, reverse=True)
if(n%2==0):
    k=n//2
else:
    k=n//2+1
print(sum(arr[:k])*2 + sum(arr[k:])*2)
