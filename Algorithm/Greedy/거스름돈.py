
# main 아이디어 거스름돈의 종류가 전부 10의배수라서 가장 큰 거스름돈먼저 계산하는게 최적의 답이라는게 보장됨
n =int(input())

coins = list(map(int, input().split()))
count = 0
coins.sort(reverse=True)

for coin in coins:
    count += n//coin
    n  %= coin
print(count)


