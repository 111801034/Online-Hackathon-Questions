xyzab = list(map(int, input().rstrip().split()))

x = xyzab[0]    #price of X burger
y = xyzab[1]    #price of Y burger
z = xyzab[2]    #price of XY burger
a = xyzab[3]    #number of X burgers
b = xyzab[4]    #number of Y burgers

#partitioned calculating of cost
partitions=0
if(a==b):
    partitions = (a*2)*z
else:    
    partitions = (min(a, b)*2)*z
    if(a>b):
        partitions+=(a-b)*x
    else:
        partitions+=(b-a)*y

#straight calculating of cost
sgt = x*a+y*b

#choosing the minimum of both costs to enjoyy party more!!!
print(min(partitions, sgt))
