N = int(input())
flag = 0

for i in range(N):
    num = i 
    digit  = 0

    if num <10:
        if i+i ==N:
            check = i
            flag = 1
            break
        
    while num > 10:
        digit += num%10
        num =num // 10
    if digit >0:
        digit += num
        if i + digit == N:
            check = i
            flag = 1
            break
if flag ==0:
    print(0)
else:
    print(check)

        