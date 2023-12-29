# https://school.programmers.co.kr/learn/courses/30/lessons/17682


# n이 작은 만큼 모든 경우를 구현
# 스택으로 구현하는데 숫자만 들어있는 리스트 활용
# 문자인경우, 10인경우, *인데 1개만 곱하는경우, 2개다 곱하는 경우
# 위의 예외들을 모두 그대로 구현
def solution(dartResult):
    answer = []
    darts = list(dartResult)
    score = ["S", "D", "T"]
    option = ["*", "#"]
    stack = []

    i = 0

    while i < len(darts):
        if darts[i] in score:
            num = int(stack.pop())
            if darts[i] == "D":
                num = num**2
            elif darts[i] == "T":
                num = num**3
            stack.append(num)

        elif darts[i] in option:
            if darts[i] == "*":
                num = stack.pop() * 2
                if len(stack) > 0:
                    prev_num = stack.pop() * 2
                    stack.append(prev_num)
                stack.append(num)
            elif darts[i] == "#":
                num = stack.pop() * -1
                stack.append(num)

        else:
            if darts[i] == "1" and darts[i + 1] == "0":
                stack.append(10)
                i += 1
            else:
                stack.append(int(darts[i]))
        i += 1
        print(stack, darts)
    return sum(stack)
