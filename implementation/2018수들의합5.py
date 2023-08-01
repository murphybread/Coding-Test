
"""
투 포인터

start와 end 구현 O(N)
internal sum = 0 -> count증가
internal_sum > -> N start 증가 및 internal_sum start만큼 감소
internal_sum < -> N end 증가 및 internal_sum end만큼 증가

"""

N = int(input())

array = []

end = 1
count = 0
internal_sum = 0

# 메모리 초과 오류
# for i in range(1,N+1):
#     array.append(i)


for start in range(1,N+1):
    while internal_sum <N and end <=N:
        internal_sum += end
        end+=1
    if internal_sum == N:
        count+=1
    internal_sum -= start
print(count)