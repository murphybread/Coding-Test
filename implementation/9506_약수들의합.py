# 2초 (2 < n < 100,000) , 
n = int(input())

while n  != -1:
    divisor = []
    line = ""
    for i in range(1, n):
        if n%i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        print(f'{n} = {divisor[0]}', end = '')
        for num in divisor[1:]:
            line += f' + {num}'
            

            #print("+", num, end= ' ')
        print(line)
        
    else:
        print(f'{n} is NOT perfect.')
    n = int(input())
    