# 이진 탐색의 경우 확인하는 숫자 자체의 범위가 매우큰 경우가 많ㅇ므
# 특정 수의 개수 구하기는 이진탐색-bisect모듈 사용하기

# 첫째 줄에 N(1<=N<=1e6(과 x(-1e9<=x<=1e9)가 정수 형태로 공백으로구분돼 입력됨
# 둘째 줄에 N개의 원소가 정수형태로 공백으로 구분 입력 -1e9<=n<=1e9
# 수열의 원소중 값이 x인 원소 개수 출력, 만약 없다면 -1 출력
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

right_index = bisect_right(array, x)
left_index = bisect_left(array, x)

if right_index - left_index == 0:
    print(-1)
else:
    print(right_index - left_index)
