N, M = map(int, input().split())
basket = [i for i in range(N + 1)]


for _ in range(M):
    i, j, k = map(int, input().split())
    basket[i : i + j - k + 1], basket[i + j - k + 1 : j + 1] = (
        basket[k : j + 1],
        basket[i:k],
    )


for b in basket[1:]:
    print(b, end=" ")
