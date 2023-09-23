# https://school.programmers.co.kr/learn/courses/30/lessons/72410
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.


# 다음부터는 단계마다 출력 확인하는 걸 표기하는게 좋은듯
def solution(new_id):
    answer = ""

    chars = [chr(i) for i in range(97, 123)]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    others = ["-", "_", "."]

    # 1 간단한 소문자 만들기 함수
    test_id = new_id.lower()

    # 2 숫자인경우 추가, 영어 소문자나 정해진 특수문자인경우 포함
    test_list = []
    for p in test_id:
        if p.isdigit():
            test_list.append(p)
            continue
        if p in chars or p in others:
            test_list.append(p)

    stack = []

    # print("2,test_list",test_list)

    # 3 '.'문자가 연속인 경우 무시
    n = 0
    while n < len(test_list):
        stack.append(test_list[n])

        if len(stack) >= 2:
            if stack[-1] == "." and stack[-2] == ".":
                stack.pop()

        n += 1

    # 4 끝이나 처음이 '.'인경우 제거
    for _ in range(len(stack)):
        if stack[0] == "." or stack[-1] == ".":
            if stack[0] == ".":
                stack.pop(0)
            elif stack[-1] == ".":
                stack.pop()

    # 5 빈리스트인경우
    if not stack:
        stack = ["a"]

    # 6 길이가 16넘을경우 15까지 처리, 마지막 문자가'.'인경우 처리
    if len(stack) >= 16:
        stack = stack[:15]
    for _ in range(len(stack)):
        if stack[-1] == ".":
            if stack[-1] == ".":
                stack.pop()
    # 7 길이가 2보다 작은경우 마지막문자 반복
    short = []
    if len(stack) <= 2:
        short = stack
        while len(short) < 3:
            short.append(stack[-1])

        return "".join(short)
    else:
        print(stack)
        return "".join(stack)
