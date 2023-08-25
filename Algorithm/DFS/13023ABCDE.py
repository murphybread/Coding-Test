"""
문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

6 5
0 1
0 2
0 3
0 4
0 5

"""

# 다음 문제가 DFS를 이용하여 깊이가 5인 관계를 나타냄을 알 수 있는지/
# 다음 관계를 그래프로 그릴 수 있는지? DFS로 구현이 가능한지?
# visited, graph list 사용
# 모든 노드를 0부터 시작해서 DFS(0~N-1)했을때 각 DFS(i)에 대해 깊이가 4(visited의 길이가 5)이면 count  + 1
# 한번 방문한 노드는 재방문 하면 안됨

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * n
count = False


def dfs(v, depth):
    global count
    if depth == 5:
        count = True
        return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[v] = False


# 값 입력받기
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


for i in range(n):
    dfs(i, 1)
    if count:
        break

if count:
    print(1)
else:
    print(0)






