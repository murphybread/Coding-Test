# Ai 값 -10억~+10억
# 문제해석 N은 2000까지, 수의 위치가 다르면 다른수 2000 2000은 다른 수
# set을 사용


# 좋은 수를 찾는다
# - (오름차순)
# - 두 개의 합임으로 num보다 작은 두 수를 투포인터로
# - 가장 작은 수와 바로 다음 수의 합이 num보다 크다면 무시
# - 가장 작은 수와 바로 다음 수의 합이 num보다 작다면 start 움직이기
# Counter로 set 형태의 중복제거 자료형을 만든다
# Counter로 좋은수가 몇개인지 센다
import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))

array.sort()
count = 0



for i in range(2,len(array)):
    start = 0
    end = 1
    internal_sum = array[start]
    while internal_sum < array[i] and end < i:
        internal_sum += array[end]
        end +=1
        if end == i-1:
            internal_sum -= start
            start += 1
            end = start +1
    if internal_sum == num:
        count +=1
print(count)        
        
    
    




