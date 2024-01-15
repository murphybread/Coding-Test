"""
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
"""


# 중요한 것은 값에서 최소공배수를 두값과 비교하기
# 그리고 값에서 / 이 아니라 // 으로 해야 float 타입에러가 안생기고 결과값도 맞음
from math import gcd


def solution(arr):
    answer = arr[0]

    for num in arr[1:]:
        answer = (answer * num) // gcd(answer, num)

    return answer
