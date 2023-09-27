# https://school.programmers.co.kr/learn/courses/30/lessons/12900

# greed나 dp인데
# dp에 가까운듯 i개의 타일로 가능한 최대 수 dp[i]

# 수 많은 시행 착오 끝에

# dp[i] 가 가능한 경우는  i-1개에서 세로타일 붙이는 경우의수 + i-2개에서 가로타일 하나 붙이는 경우의수
# dp[i] = dp[i-1] + dp[i-2]

# 점화식으로 설명하면 n*가로 타일링의 dp는 길이 1빼는 경우 + n길이 만큼 빼는 경우
# dp[i] = dp[i-1] + dp[i-n]


def solution(n):
    MOD = 1_000_000_007  # Modulo constant
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 1  # One vertical tile
    dp[2] = 2  # Two vertical tiles or one horizontal tile

    # DP loop
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]
