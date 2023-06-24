a_one, a_zero = map(int,input().split())
c =int(input())
n_zero =int(input())
check =0

for i in range(n_zero ,101):
    if a_one * i +a_zero > c * i:
        print(0)
        check = 1
        break
if check == 0 :
    print(1)