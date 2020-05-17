li = list(map(int, input().rstrip().split()))
    if((li[2]-1)<=li[0]+li[1]):
        ans=(li[2]+li[1])
    else:
        ans=(li[1]+li[0]+li[1]+1)
    print(ans)
