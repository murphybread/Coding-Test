# https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
"""


# 모든 원소를 탐색하기에는 1백만은 부담됨
# 접두어의 경우 작은 길이의 번호가 큰 길이의 번호에 포함됨
# 중복은 없음
# 이건 startswith를 알아야 풀 수 있을듯.

def solution(phone_book):
    phone_book.sort()  # 리스트를 먼저 정렬합니다. 이로인해 앞으로의 알고리즘에 예왹 사라짐

    # 단순하게 앞의 문자열이 다음 문자열의 접두사로 시작하는지 여부를 탐색하는 함수 사용
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True
