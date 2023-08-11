# N X N 좌표평면을 이동하는 Implemetation 중 Simulation 문제


# 입력받기
N = int(input())
direction = input().split()

# map그리기
map = [[i for i in range(N)] for i in range(N)]
x = 0
y = 0


# 좌표 시뮬레이션 구현
move = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# direction으로부터 move mapping

for d in direction:
    nx = x + dx[move.index(d)]
    ny = y + dy[move.index(d)]

    # map벗어나는 경우는 예외 처리
    if nx >= N or nx < 0:
        continue
    if ny >= N or ny < 0:
        continue
    x, y = nx, ny


print(x + 1, y + 1)
