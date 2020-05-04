def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
    
def solution():
    # Write your code here
    n = int(input())
    int_arr = list(map(int, input().split()))
    num1 = int_arr[0]
    num2 = int_arr[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, n):
        lcm = find_lcm(lcm, int_arr[i])
    print(lcm)

# T = int(input())
T = 1
for _ in range(T):
    solution()
