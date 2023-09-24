"""
우선순위 큐는 값이 특정 조건에 따라 정렬 된 큐로서 그 조건이 다양할 수 있음
일반적으로 가장 작은 값 또는 가장 큰 값으로 정렬할 때가 많아서 이 경우 Heap구조로 구현하면 편함

Heap 구조
완전 이진 트리 형태로 1개의 원소에 대해 삽입 O(logn), 제거 O(logn) 만큼의 시간복잡도 보장
기본 파이썬의 Heap구조는 루트노드가 가장 작은 최소 힙 구조

삽입 프로세스
가장 최하단에 값 삽입 후 부모노드와 값을 비교하여 작을 경우 위치를 바꿈.
해당 프로세스가 수행이 안 될 때까지(최소 Heap을 만족할 때 까지) 수행

제거 프로세스
루트노드와 가장 마지막 노드를 교체후 하향식으로 Heap구조로 만듬


    
"""
import sys
import heapq

input = sys.stdin.readline


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 힙에 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))


res = heapsort(arr)

for i in range(n):
    print(res[i])
