# 9 8
# CCTGGATTG
# 2 0 1 1

# 슬라이딩 윈도우 start 0 end= P, 두 값이 한 칸씩 이동, P가 N-1이 될 때까지
# {A:, T, C, G} 딕셔너리에 입력 값 선언
# 각 부분 집합마다 딕셔너리 값과 비교, 만약 true라면 count +1


# count함수가 시간초과의 원인으로 판단.
# 처음부터 collection함수로 구하기
from collections import Counter
import sys
input = sys.stdin.readline


S, P = map(int, input().split())
DNA = input().strip()
DNA_A, DNA_C, DNA_G, DNA_T = map(int,input().split())
condition= Counter(DNA)
condition["A"] = DNA_A
condition["C"] = DNA_C
condition["G"] = DNA_G
condition["T"] = DNA_T

start = 0
end = P
count = 0

while end <= S:
    
    partial = Counter(DNA[start:end])
    
    diff = condition - partial
    print(diff)
    # If the diff Counter has no elements, then partial satisfies the condition
    if not diff:
        count += 1

    start += 1
    end += 1
print(count)
