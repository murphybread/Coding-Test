import sys
input = sys.stdin.readline

m =2
N = int(input())
while N!=1:
    if N%m == 0:
        print(m)
        N =N/m
    else:
        m +=1

