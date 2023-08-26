"""
https://school.programmers.co.kr/learn/courses/30/lessons/43165
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""


# 문제 탐색
# 각 더하기 빼기 상태 값을 저장
# 단순 더하기 빼기 연속이기에 재귀적
# 가능한 모든 수이기에 탐색 방식


# 구현
# 리스트에 [값,인덱스], [-값,인덱스] 형태로 저장
# while stack 및 if 인덱스 < n 및 else사용
# else의 경우 최종적으로 모든수를 더하거나 뺀 값으로 target값과 비교


def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-numbers[0], 0]]
    n = len(numbers)

    while stack:
        temp, idx = stack.pop()
        idx += 1

        if idx < n:
            stack.append([temp + numbers[idx], idx])
            stack.append([temp - numbers[idx], idx])

        else:
            if temp == target:
                answer += 1

    return answer