def lca(a, b):
    while d[a] != d[b]:
        if d[b] > d[a]:
            b = parents[b]
        else:
            a = parents[a]

    while a != b:
        b = parents[b]
        a = parents[a]

    return a


def dfs(x, depth):
    c[x] = True
    d[x] = depth

    for y in graph[x]:
        if c[y]:
            continue
        parents[y] = x
        dfs(y, depth + 1)


import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)

n = int(input())

parents = [0] * (n + 1)
c = [0] * (n + 1)
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1, 0)


m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))


# 다녀갔는지 체크
# 깊이표현
# 그래프만들기
