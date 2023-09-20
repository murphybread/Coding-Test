"""
서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조이다.
서로소 집합 자료구조는 두 종류의 연산을 지원한다.
합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이다.
찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다.
서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도 한다.
여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같습니다.

"""


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if b > a:
        parent[b] = a
    else:
        parent[a] = b


def find(parent, x):
    if parent[x] != x:
        print("before", x)
        parent[x] = find(parent, parent[x])
        print("after", parent[x])
    return parent[x]


v, e = map(int, input().split())


parents = [0] * (v + 1)

for i in range(1, v + 1):
    parents[i] = i


for i in range(e):
    a, b = map(int, input().split())
    union(parents, a, b)

print("각 원소집합", end=" ")
for i in range(1, v + 1):
    print(find(parents, i), end=" ")

print()


print("부모테이블")
for i in range(1, v + 1):
    print(parents[i], end=" ")
