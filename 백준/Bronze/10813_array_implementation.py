N, M =map(int, input().split())
basket= [i for i in range(N+1)]

for _ in range(M):
    i, j =map(int, input().split())
    basket[i],basket[j] =basket[j],basket[i]

for n in basket[1:]:
    print(n, end =" ")
