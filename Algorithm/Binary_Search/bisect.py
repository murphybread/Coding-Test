from bisect import bisect_left, bisect_right


# 특정 범위 속하는 연속된 수의 인덱스 범위 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(left_index, right_index)
    return right_index - left_index


# 탐색 배열
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터의 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1,3] 범위의 데이터 출력
# left index -1보다 큰 첫번째 원소 위치 0 반환
# 3보다 큰 첫번째 원소인 4가 처음으로 나오는 인덱스 6 반환
print(count_by_range(a, -1, 3))
