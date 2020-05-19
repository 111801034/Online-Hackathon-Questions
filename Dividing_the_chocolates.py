# cook your dish here

X, Y, Z = input().split()
X = int(X)
Y = int(Y)
Z = int(Z)
action = 0
while(True):
    if X == Y and Y == Z:
        action = -1
        break
    elif X%2 == 0 and Y%2 == 0 and Z%2 == 0:
        temp_X = int(Y/2) + int(Z/2)
        temp_Y = int(X/2) + int(Z/2)
        temp_Z = int(X/2) + int(Y/2)
        action = action + 1
    else:
        break
    X = temp_X
    Y = temp_Y
    Z = temp_Z
print(action)
