import math
A,B,V = map(int,input().split())

diff = A-B


n= math.ceil((V-A) / diff)
print(n+1)