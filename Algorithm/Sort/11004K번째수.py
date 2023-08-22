# N <= 5,000,000 임으로 O(nlogn)으로시도
# sort 후 배열[K] 출력
N, K = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
print(arr[K - 1])
