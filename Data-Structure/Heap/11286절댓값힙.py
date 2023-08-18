import heapq
import sys

input = sys.stdin.readline

# 힙구조임으로 힙 리스트 선언
N = int(input())
heap = []


# 우선순위를 가장 절대값이 작은 값으로 선정
# heapq.heappush에대한 key값으로 설정
for _ in range(N):
    i = int(input())
    if i == 0 and len(heap) == 0:
        print(0)
    elif i == 0 and len(heap) != 0:
        # heappop시 먼저값인 abs(i)값을 기준으로 하기에 절대값이 min heap이라 절대값이 작은 값 선정
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(-i), i))
    print(heap, "A")


# 예외처리 값이 없을 때
