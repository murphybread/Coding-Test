# https://school.programmers.co.kr/learn/courses/30/lessons/118666

# 위 예시처럼 네오형이 비동의, 어피치형이 동의인 경우만 주어지지 않고, 질문에 따라 네오형이 동의, 어피치형이 비동의인 경우도 주어질 수 있습니다.
# 꼭 포지션이 정해진건 아님

# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단합니다.

# 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.

# 구현

# choice에서 4점 빼기 만약 양수 라면 i[1], 음수라면 i[0]를 더해주기


# 각 점수를 dict로 더해주기
# 나중에 2개씩 비교해서 값높은 걸로 뽑기, 같은값이면 사전순으로 뽑기
def solution(survey, choices):
    answer = ""
    # result = [{'R':0}, {'T':0}, {'C':0},{'F':0}, {'J':0},{'M':0},{'A':0} ,{'N':0} ]
    result = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # i[0] 비동의+3 , i[1] 동의 +3
    print(survey)

    i = 0
    for num in choices:
        check = num - 4
        if check > 0:
            result[survey[i][1]] += check

        elif check < 0:
            result[survey[i][0]] += -check

        else:
            pass
        i += 1

    r = list(result.items())
    for i in range(0, 7, 2):
        a = r[i][1]
        b = r[i + 1][1]

        a_char = str(r[i][0])
        b_char = str(r[i + 1][0])

        if a > b:
            answer += a_char
        elif b > a:
            answer += b_char
        else:
            answer += chr(min(ord(a_char), ord(b_char)))

    return answer
