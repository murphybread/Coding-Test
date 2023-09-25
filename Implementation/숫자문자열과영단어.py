# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 문자 '1' 49 부터 '9'까지 57
# 49부터 57까지를 통해 문자인지 판별하고
# 만약 숫자면 result에 숫자 더해주고
# 만약 문자면 += 하고 만약 정해진 알파벳에 있으면 숫자로 바꿔서 result에 더해주기


# 케이스10에러
def solution(s):
    result = []
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    stra = ""

    for i in s:
        if 48 <= ord(i) <= 57:
            result.append(int(i))
        else:
            stra += i
            if stra in words:
                result.append(int(words.index(stra)))
                stra = ""

    answer = ""
    for r in result:
        answer += str(r)

    return int(answer)
