# M <=23 이기에 O(N^3) 가능


# 입력받기
N = int(input())

# 3이 등장한 횟수 저장 변수
count = 0

# 0-N 시간, 0-59분, 0-59초로 확인
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if "3" in time:
                count += 1

print(count)
