# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# 1 3 4     [3 4], [6,8]
# 2
# i*j j*k ->  i*k
def solution(arr1, arr2):
    A_i = len(arr1)
    A_j = len(arr1[0])
    A_k = len(arr2[0])
    answer = [[0] * A_k for _ in range(A_i)]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j] * arr2[j][k]
                # print(i,j,k,arr1[i][j] *arr2[j][k])
                # answer[i].append(arr1[i][j] *arr2[j][k])

    return answer
