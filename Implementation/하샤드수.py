# https://school.programmers.co.kr/learn/courses/30/lessons/12947

# 구현
# 처음 수 저장
# 자리수와몫 고려
# 마지막 while을 탈출하는 10이하의 상태 고려

def solution(x):
    """
    문제 설명
    양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

    제한 조건
    x는 1 이상, 10000 이하인 정수입니다.
    """
    first = x
    section = 0

    while x // 10 >= 1:
        section += x % 10
        x = x // 10
    section += x % 10

    if first % section == 0:
        return True
    else:
        return False