# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# bfs

from collections import deque

def solution(maps):
    # 4방향을 확인하기위한 튜플 리스트
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    # 시작위치를 튜플쌍(x,y)으로 받고 목적지도 동일한 구조로 받음. visited의경우 S->L과 L->E를 따로 구분함
    def bfs(start, end, visited):
        # bfs를 활용하기 위해 queue에 넣음
        queue = deque([(start, 0)])
        while queue:
            (x, y), dist = queue.popleft()
            # 도착할 경우 return 이동한 시간
            if (x, y) == end:
                return dist
            # 상화좌우를 확인
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 먼저 맵을 벗어나는지 확인
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):

                    # 맵을 안 벗어난 상태에서 방문했는지 and 벽인지 확인
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        # 방문 처리
                        visited[nx][ny] = True
                        # 다음 위치를 queue에 넣은 후 길이를 증가
                        queue.append(((nx, ny), dist + 1))
        return -1

    start, lever, exit = None, None, None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # S-L당시의 visited로 구현
    visited1 = [[False] * len(maps[0]) for _ in range(len(maps))]
    dist_lever = bfs(start, lever, visited1)
    if dist_lever == -1:
        return -1

    # L-E당시의 visited로 구현
    visited2 = [[False] * len(maps[0]) for _ in range(len(maps))]
    dist_exit = bfs(lever, exit, visited2)
    if dist_exit == -1:
        return -1

    return dist_lever + dist_exit
