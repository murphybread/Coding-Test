# 첫째 줄 떡의개수 N(1<=N<=1,000,000) 과 떡의 길이 M (1<=M<=2,000,000,000) 절단기 높이는 10억 이하 양수
# 둘째 줄에는  각 떡의 높이
# 최소 M만큼의 떡을 집에가져가기위한 절단기 높이 최대값

# 아이디어는 10억이라는 큰 수인 만큼 Log를 취해야하는 이진 탐색으로 고려
# 이진 탐색에서도 만약 조건에해당하면 예,아니오에 따라 다음 조건 수행

# 가징 긴 길이의 절반을 자르는 위치로 시작
# 잘린 떡의 길이 합계산
# 만약 잘린떡이 M보다 크다면 자르는 위치 이동
# 만약 잘린떡이 M보다 작다면 이전으로 이동
# 계속해서 잘린떡이 M보다 크다는걸 처음부터 보장하기 때문

# 변수 입력 받기
N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))

# 잘린떡 변수체크, 처음 자르는 위치 및 시작,끝 설정
check = 0
start = 0
end = max(rice_cake)


while start <= end:
    sum = 0
    h = (start + end) // 2

    for x in rice_cake:
        if x > h:
            sum += x - h
    if sum < M:
        end = h - 1
    # sum >=M 이라는 뜻임으로 일단 해당 위치 체크 및 더 자를 수 있나 start 이동
    else:
        start = h + 1
        check = h
print(check)
