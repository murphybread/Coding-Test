# 1번과 2번 중 2번의 방법이 확실히 시간복잡도를 줄일 수 있음
# "가능한한" 2번을 수행 하고  안 되면 1번 수행
# while조건으로 N !=1
# 수행마다 count++

N, K = map(int, input().split())
count = 0

while N != 1:
    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1
print(count)
