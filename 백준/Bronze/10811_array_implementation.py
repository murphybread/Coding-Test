N, M = map(int, input().split())

basket = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    while i < j:
        basket[i], basket[j] = basket[j], basket[i]
        j -= 1
        i += 1


for ball in basket[1:]:
    print(ball, end=" ")
