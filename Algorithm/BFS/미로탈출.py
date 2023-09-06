"""
NxM크기의 미로
출발위치는 (1,1) 출구는 (N,M) 괴물은 0, 통로는 1
최소탈출하기 위한 칸의 개수, 시작칸과 마지막칸 고려
"""


# 최소칸 즉 BFS문제
# 2차원 미로 받기
# bfs에서 예외 칸을벗어남, 0일경우 제외
# 상하좌우를 위한 nx,ny설정
from collections import deque

def bfs(x,y):

    queue =deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))


    return graph[n-1][m-1]

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))
