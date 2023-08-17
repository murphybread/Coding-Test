# N<=100,000이기에 O(N logN)을 보장해야함
# min, max로 접근할시 해당 함수가 O(N) , N번 반복임으로 O(N^2)
# 처음부터 A정렬을 오름차순, B정렬을 내림차순으로  바꾼 후 비교

# 입력받기
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# O(N log N)으로 정렬
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    # 만약 A의 모든원소값이 B보다 큰 경우
    else:
        break

print(sum(A))
