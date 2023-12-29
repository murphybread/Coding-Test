"""
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
입출력 예
s	return
"3people unFollowed me"	"3people Unfollowed Me"
"for the last week"	"For The Last Week"
"""


def solution(s):
    answer = ""
    s_list = s.split(" ")  # 공백을 기준으로 나누되, 연속된 공백도 처리

    print("    a  s     ".split(" "))

    for words in s_list:
        if words:  # 빈 문자열이 아닐 경우에만 처리
            answer += words[0].upper() + words[1:].lower() + " "
        else:
            answer += " "  # 원본 문자열의 연속된 공백 처리

    return answer[:-1]  # 마지막에 추가된 불필요한 공백 제거
