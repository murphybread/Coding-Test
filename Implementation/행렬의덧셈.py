# https://school.programmers.co.kr/learn/courses/30/lessons/12950

# 보자마자 단순히 더하면 되겠다는 생각이듬
# 추가로 따로 배열 만들 필요없이 기존 배열 사용방법
# N=500일경우 N^2  = 250000 이기에 O(N^2) 허용
def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr2[i][j] += arr1[i][j]

    return arr2