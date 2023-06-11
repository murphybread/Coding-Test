import sys
input = sys.stdin.readline

M=int(input())
N=int(input())

primes = []
check = 0  

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i%j ==0:
            check =1
            break
    if check != 1:
        primes.append(i)
    else:
        check =0

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))