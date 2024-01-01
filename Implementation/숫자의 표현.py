"""
문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
"""


def solution(n):
    answer = 0

    left, right = 1, 1
    # 투포인터 적으면 LEFT +1 , 크면 Right-1, 같은면 count +1 하고 left1
    # main point는 sub_sum을 3가지경우에 대해 업데이트해주기, right의 경우 right업데이트후 값반영, left의 경우 -후 left 업데이트

    sub_sum = 1

    c = 0
    while right <= n:
        if sub_sum < n:
            right += 1
            sub_sum += right
        elif sub_sum == n:
            answer += 1
            sub_sum -= left
            left += 1

        elif sub_sum > n:
            sub_sum -= left
            left += 1

    return answer
