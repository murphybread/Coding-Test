# 오름차순 정렬
# 부분합 이용

# sort()
# s[i] = s[i-1] +A[i]

N = int(input())
atm = list(map(int, input().split()))
s = [0] * N

atm.sort()
s[0] = atm[0]

for i in range(1, N):
    s[i] = s[i - 1] + atm[i]

print(sum(s))
