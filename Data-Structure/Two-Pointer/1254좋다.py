# Ai 값 -10억~+10억
# 문제해석 N은 2000까지, 수의 위치가 다르면 다른수 2000 2000은 다른 수

# 좋은 수를 찾는다
# - (오름차순 정렬)
# - start를 0, end를 N-1로 원소의 왼쪽 끝에서 오른쪽 끝을 가리키는 투 포인터 선언
#   - 여기서 헤맸던 부분은 end를 가리키는 i-1로 해야하는 것 아닌가? 였는데  숫자의범위가 -가 포함돼서 오른쪽 끝이 맞음
#      - test case -4 0 4, start가 0번째 원소, end가 N-1일 경우에야 count가 됨
# - i가 start나 end일 때는 pass
# N =2000이기에 O(N) 가능. sort함수 O(NlogN)


N = int(input())
array = list(map(int, input().split()))

array.sort()
count = 0

for i in range(N):
    start = 0
    end = N - 1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        
        internal_sum = array[start] + array[end]
        
        if internal_sum == array[i]:
            count += 1
            break
        elif internal_sum < array[i]:
            start += 1
        else:
            end -= 1

print(count)

    
    




