S = input()
K = input()
K = int(K)
l = len(S)
li = []
for k in range(0,l):
    li.append(S[k])
if len(set(li)) == 1:
    print(int((l*K)/2))
else:
    i = 0
    count = 0
    temp = 0
    if l == 1:
        ans = K/2
        print(int(ans))
    else:
        while(0 <= i <= l-1):
            if i == l-1:
                if S[i] == S[0]:
                    temp = 1
                    break
                else:
                    break
            elif S[i] == S[i+1]:
                i = i+2
                count = count + 1
            else:
                i = i + 1
        if temp != 1:
            print(count*K)
        else:
            print(count*K + K-1)
