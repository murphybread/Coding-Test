# 8*8 좌표평면 이동 implementation-simulation
import time

# string입력 받기
s = input()
table = [[i for i in range(1, 9)] for i in range(1, 9)]

# 이동 할 수 있는 경우의 수 전부 구해놓기
move = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, -2], [-1, 2], [-2, -1], [-2, 1]]
# 방법 저장 변수
count = 0


# 현재위치 숫자처리
x = int(s[1])
y = ord(s[0]) - 96
# for문으로 해당 경우의수 전부 계산 해서 만약 좌표평면 안 이라면 count++

for m in move:
    nx = x + m[0]
    ny = y + m[1]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1


print(count)


# 깨달은점 table 즉 8*8을 선언할 필요가 없음
