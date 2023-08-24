"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
"""

# 연결 요소의 개수 DFS임을 파악
# 이번엔 재귀함수로 구현. node가 1000개임으로 N^2도되지만  DFS구현시 O(n+e)

# sys 모듈로부터 파이썬 재귀리미트 및 입력 속도 개선 설정
# graph 저장 리스트, 방문 리스트, dfs 선언
# 1부터n까지 dfs(i)구현 하며 만약 visited i 가 False인경우 count(연결 요소 개수)+1


import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 초기 입력 및 그래프 리스트, 방문 리스트, 연결요소 저장 변수 선언
n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0


def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)


# edge 입력받아 인접리스트 채우기
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)
