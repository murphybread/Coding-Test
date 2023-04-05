N, M = map(int, input().split())


basket = [0] * (N + 1)

for num in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        basket[index] = k

for ball in basket[1:]:
    print(ball)
