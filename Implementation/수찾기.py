"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5

예제 출력 1 
1
1
0
0
1
"""

# O(N*M)형태일경우 시간초과. M을 N찾을 때마다 하면 다음과같음

# 이분 탐색

# 또는 set를 활용. in연산자의 경우 리스트에서는 O(n)이기에 m번 반복할경우 O(n*m)이지만
# set은 in연사자의 경우 해시기반으로 되어있어 일반적으로 O(1)을 갖기에 set에서는 O(n) + O(m)  이됨
n = int(input())
arr = list(map(int, input().split()))
arr_set = set(arr)  # Convert to set for O(1) lookup

m = int(input())
check = list(map(int, input().split()))

for num in check:
    print(1 if num in arr_set else 0)
