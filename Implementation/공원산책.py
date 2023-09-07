# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# 구현
# 두가지 요소 고려
# 반환값은 최종 위치

# NSWE 배열 선언

# 가장 많이 시간 걸린 부분. 해당 사항인 경우 break 하고 마지막에 반영여부 결정
# x,y를 기존값에여러번 추가하는 방식

def solution(park, routes):
    answer = []

    row = len(park)
    col = len(park[0])

    # NSWE는 x,y좌표
    ways = ['N', 'S', 'W', 'E']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 숫자만큼 추가 행동

    # 시작 위치 확인
    for i in range(row):
        for j in range(col):
            if park[i][j] == 'S':
                start = [i, j]

    x, y = start[0], start[1]

    for route in routes:
        hit = 0
        nx, ny = x, y

        for _ in range(int(route[2])):

            nx += + dx[ways.index(route[0])]
            ny += + dy[ways.index(route[0])]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                hit = 1
                break

            if park[nx][ny] == 'X':
                hit = 1
                break

        if hit == 0:
            x, y = nx, ny

    return [x, y]