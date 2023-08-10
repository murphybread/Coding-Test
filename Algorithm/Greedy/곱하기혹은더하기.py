# 그리디인지 파악
# 더하기와 곱하기 중 곱하기를 최대한 많이하기
# 곱하기가 더하기에 비해값을 최대로 할 수 있는 방법

# 단 조건으로 입력받는 수가 1 이하이면 +
# 값을 저장하는 변수 선언
# 만약 sum이 0이고 array가 2이상이라면 곱하기 0으로 처리되서 해당 사항 처리


array = input()
sum = int(array[0])

for i in array[1:]:
    i = int(i)
    if i <= 1 or sum <= 1:
        sum += i
    else:
        sum *= i


print(sum)
