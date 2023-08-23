"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

# N의 크기가큼. 대신 최대값이 10000이하임. O(nlogn)보다 빠른 O(kn)인 기수 정렬(radix sort) 사용
# 기수 정렬의 경우 최대 값이 작을 때 사용
import sys

input = sys.stdin.readline

# 10001크기 리스트선언
array = [0] * 10001

N = int(input())

for _ in range(N):
    n = int(input())
    array[n] += 1

for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)
