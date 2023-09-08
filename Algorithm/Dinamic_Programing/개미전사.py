N =int(input())
stores = list(map(int,input().split()))


# dp[i]는 i번째 까지 얻은 최적의 해
dp = [0] * len(stores)

dp[0] = stores[0]
dp[1] = max( stores[1],stores[0])


for i in range(2,len(stores)):
    dp[i] = max(stores[i] + dp[i-2], dp[i-1])

print(dp[N-1])