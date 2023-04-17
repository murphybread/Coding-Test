import sys
input = sys.stdin.readline

N, B = input().split()
A = []
B = int(B)

for n in N:
    if n.isalpha():
        num = ord(n) - 55
        A.append(num)
    else:
        A.append(int(n))
    
A.reverse()


acc = 0
for i in range(len(A)):
    acc += A[i] * B**i
print(acc)
