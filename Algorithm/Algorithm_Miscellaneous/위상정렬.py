from collections import deque


v, e = map(int, input().split())


q = deque()
graph = [[] for _ in range(v + 1)]
distance = [0] * (v + 1)

result = []

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    distance[b] += 1

for i in range(1, v + 1):
    if distance[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    result.append(now)

    for d in graph[now]:
        distance[d] -= 1
        if distance[d] == 0:
            q.append(d)

print(result)
