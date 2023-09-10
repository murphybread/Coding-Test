"""
N가지 종류의 화폐로 M원을 만들 때
M원을 만들기 위한 최솟값

"""

# 불가능할 때는 -1

n,m = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# 무한대 값
dp = [10001] * 10001 # M원을 만들기 위한 최소 동전 개수


#dp 시도
# coins의 값을 확인하는 for문과
# 만들어진 금액 합계 for문을 사용

# 0원을 만드기위한 방법은 0개임으로 초기화. 초기화 해놓아야 이후 맨처음 coin이 등장할때 0+1형태로 1개가 초기화 됨

dp[0]=0
for coin in coins:
    for j in range(coin,m+1):
        print(j, j-coin)
        if dp[j-coin] != 10001:
            dp[j] = min(dp[j], dp[j-coin]+1)




if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])