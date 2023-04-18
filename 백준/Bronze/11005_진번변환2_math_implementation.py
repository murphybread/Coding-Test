N, B = map(int, input().split())
A = []
B = int(B)


while N > 0:
    N, num = N // B, N % B
    A.append(num)


output = ""
for i in range(len(A)):
    if A[i] >= 10:
        output += chr(A[i] + 55)
    else:
        output += str(A[i])
print(output[::-1])
