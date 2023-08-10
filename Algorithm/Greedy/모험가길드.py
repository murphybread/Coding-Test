# 구현? 그리디?
# N은 10만이라 O(N) 충분
# 그룹의최댓값을 구하기 위해 오름차순 정렬 필요

# 부분집합의 최솟값이, 부분집합의 길이이상이면 count++


N = int(input())
guild = list(map(int, input().split()))
count = 0
subset = 0
guild.sort()

for i in range(len(guild)):
    subset += 1

    if subset >= i:
        subset = 0
        count += 1


print(count)
