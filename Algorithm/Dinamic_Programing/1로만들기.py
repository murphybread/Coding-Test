"""

첫째줄에 정수 x가 주어질때 1<=x<=30000
첫째줄에 연산 최소 횟수 출력

연산은 5나누기 3나누기 2나누기 1빼기만가능
"""



# dp활용


n = int(input())
count = 0
# 최악의 경우 1빼기 n 번하면 되니깐 n크기 선언
dp = [0] * (n+1)




# dp[i]번째 값은
# 각 경우의 해당 값에 count

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i %2 ==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i %3 ==0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i %5 ==0:
        dp[i] = min(dp[i], dp[i//5] + 1)
print(dp[n])