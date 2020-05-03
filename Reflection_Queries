def solution(coords, query):
    # Write your code here
    l = int(query[1])
    h = int(query[2])
    h = min(h, n)
    l = max(l, 1)
    if(query[0]=='X' or query[0]=='x'):
        for i in range(l-1, h):
            coords[i][1]*=(-1)
    elif(query[0]=='Y' or query[0]=='y'):
        for i in range(l-1, h):
            coords[i][0]*=(-1)
    elif(query[0]=='C' or query[0]=='c'):
        quadrants = {1:0, 2:0, 3:0, 4:0}
        for i in range(l-1, h):
            x = coords[i][0]
            y = coords[i][1]
            if((x>=0 and y>=0)):
                quadrants[1]+=1
            if(x<=0 and y>=0):
                quadrants[2]+=1
            if(x<=0 and y<=0):
                quadrants[3]+=1
            if(x>=0 and y<=0):
                quadrants[4]+=1
        print("{} {} {} {}".format(quadrants[1], quadrants[2], quadrants[3], quadrants[4]))

n = int(input())
coords = []
for i in range(n):
    coord = list(map(int, input().split()))
    coords.append(coord)
q = int(input())
for i in range(q):
    query = input().rstrip().split()
    solution(coords, query)
